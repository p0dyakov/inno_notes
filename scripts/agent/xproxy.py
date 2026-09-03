"""Local CONNECT forwarder: Google API hosts dial via xbox-dns IPs, rest direct."""
import base64, re, socket, struct, threading, urllib.request, json

DOH = 'https://xbox-dns.ru/dns-query?dns='
XHOSTS = ('googleapis.com', 'gstatic.com', 'google.com')

_cache = {}
def xbox_A(host):
    if host in _cache: return _cache[host]
    q = b'\x22\x22\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' + b''.join(bytes([len(p)])+p for p in host.encode().split(b'.')) + b'\x00' + struct.pack('>HH', 1, 1)
    url = DOH + base64.urlsafe_b64encode(q).rstrip(b'=').decode()
    req = urllib.request.Request(url, headers={'Accept': 'application/dns-message'})
    raw = urllib.request.urlopen(req, timeout=15).read()
    ips = ['.'.join(map(str, m)) for m in re.findall(rb'\x00\x04([\x00-\xff]{4})', raw)
           if not m.startswith(b'\x00\x00')]
    # filter junk: keep plausible public v4
    ips = [ip for ip in ips if not ip.startswith(('0.', '10.', '127.', '192.168.', '172.16.'))]
    _cache[host] = ips
    print('xbox', host, '->', ips, flush=True)
    return ips

def pipe(a, b):
    try:
        while True:
            d = a.recv(65536)
            if not d: break
            b.sendall(d)
    except Exception: pass

def handle(conn):
    try:
        head = b''
        while b'\r\n\r\n' not in head:
            d = conn.recv(4096)
            if not d: conn.close(); return
            head += d
        line = head.split(b'\r\n')[0].decode()
        _, target, _ = line.split(' ')
        host, port = target.rsplit(':', 1)
        ips = None
        if host.endswith(XHOSTS):
            try: ips = xbox_A(host)
            except Exception as e: print('doh fail', host, e, flush=True)
        cands = (ips or []) + [(host, int(port))]
        out = None
        for cand in cands:
            try:
                ip = cand if isinstance(cand, str) else cand[0]
                out = socket.create_connection((ip, int(port)), timeout=15)
                print(f'CONN {host}:{port} via {ip}', flush=True)
                break
            except Exception: continue
        if out is None:
            conn.sendall(b'HTTP/1.1 502 Bad Gateway\r\n\r\n'); conn.close(); return
        conn.sendall(b'HTTP/1.1 200 Connection Established\r\n\r\n')
        t = threading.Thread(target=pipe, args=(conn, out), daemon=True); t.start()
        pipe(out, conn)
    except Exception: pass
    finally:
        try: conn.close()
        except Exception: pass

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(('127.0.0.1', 18081))
srv.listen(50)
print('xproxy on 127.0.0.1:18081', flush=True)
while True:
    c, _ = srv.accept()
    threading.Thread(target=handle, args=(c,), daemon=True).start()
