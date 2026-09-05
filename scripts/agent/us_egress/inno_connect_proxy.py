"""Single-threaded HTTP CONNECT proxy (selectors, no threads) for US-egress tests.

Localhost-only 127.0.0.1:18081, restricted to TCP/443 of Google API hosts.
All diagnostics go to stdout (systemd journal).
"""
import selectors
import socket
import sys

LISTEN = ("127.0.0.1", 18081)
ALLOWED_SUFFIXES = ("googleapis.com", "google.com", "gstatic.com")
BUF = 65536

def log(*a):
    print(*a, flush=True)

def allowed(host, port):
    h = host.lower().strip("[]")
    return port == 443 and h and any(h == s or h.endswith("." + s) for s in ALLOWED_SUFFIXES)

def resolve4(host, port):
    infos = socket.getaddrinfo(host, None, socket.AF_INET, socket.SOCK_STREAM)
    errs = []
    for _, _, _, _, sa in infos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(False)
        try:
            s.connect((sa[0], port))
        except BlockingIOError:
            pass
        except OSError as e:
            errs.append(str(e))
            s.close()
            continue
        return s
    raise OSError(f"no route to {host}: {errs[:2]}")

class Conn:
    def __init__(self, sel, client):
        self.sel = sel
        self.client = client
        self.client.setblocking(False)
        self.upstream = None
        self.buf = b""
        self.out = {client: b""}
        sel.register(client, selectors.EVENT_READ, self.on_client)

    def close(self):
        for s in (self.client, self.upstream):
            if s is not None:
                try:
                    self.sel.unregister(s)
                except Exception:
                    pass
                try:
                    s.close()
                except OSError:
                    pass

    def on_client(self, sock, mask):
        try:
            data = sock.recv(4096)
        except OSError:
            self.close()
            return
        if not data:
            self.close()
            return
        self.buf += data
        if b"\r\n\r\n" not in self.buf:
            if len(self.buf) > 65536:
                self.close()
            return
        try:
            line = self.buf.split(b"\r\n", 1)[0].decode("latin1")
            method, target, _ = line.split(" ")
            host, _, port_s = target.rpartition(":")
            port = int(port_s)
        except ValueError:
            self.close()
            return
        if method.upper() != "CONNECT" or not allowed(host, port):
            try:
                sock.sendall(b"HTTP/1.1 403 Forbidden\r\n\r\n")
            except OSError:
                pass
            self.close()
            return
        try:
            up = resolve4(host, port)
        except OSError as e:
            log("resolve/connect fail", host, e)
            try:
                sock.sendall(b"HTTP/1.1 502 Bad Gateway\r\n\r\n")
            except OSError:
                pass
            self.close()
            return
        self.upstream = up
        self.pend_host, self.pend_port = host, port
        self.sel.register(up, selectors.EVENT_WRITE, self.on_connect)
        self.buf = b""
        self.on_client = self.on_relay_client
        self.sel.modify(sock, selectors.EVENT_READ, self.on_relay_client)

    def on_connect(self, sock, mask):
        err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        if err != 0:
            log("connect fail", self.pend_host, OSError(err, "connect"))
            try:
                self.client.sendall(b"HTTP/1.1 502 Bad Gateway\r\n\r\n")
            except OSError:
                pass
            self.close()
            return
        try:
            self.client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        except OSError:
            self.close()
            return
        log("tunnel", self.pend_host, self.pend_port)
        self.buf = b""
        self.sel.modify(sock, selectors.EVENT_READ, self.on_upstream)
        self.sel.modify(self.client, selectors.EVENT_READ, self.on_relay_client)

    def relay(self, src, dst):
        try:
            data = src.recv(BUF)
        except OSError:
            self.close()
            return
        if not data:
            self.close()
            return
        try:
            dst.sendall(data)
        except OSError:
            self.close()

    def on_relay_client(self, sock, mask):
        self.relay(self.client, self.upstream)

    def on_upstream(self, sock, mask):
        self.relay(self.upstream, self.client)

def main():
    sel = selectors.DefaultSelector()
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(LISTEN)
    srv.listen(64)
    srv.setblocking(False)
    sel.register(srv, selectors.EVENT_READ, None)
    log("listening on %s:%d" % LISTEN)
    while True:
        for key, mask in sel.select(timeout=60):

            if key.data is None:
                client, _ = srv.accept()
                log("accepted", client.getpeername())
                try:
                    Conn(sel, client)
                except OSError:
                    try:
                        client.close()
                    except OSError:
                        pass
            else:
                try:
                    key.data(key.fileobj, mask)
                except Exception as e:
                    log("conn error:", repr(e)[:200])

if __name__ == "__main__":
    main()
