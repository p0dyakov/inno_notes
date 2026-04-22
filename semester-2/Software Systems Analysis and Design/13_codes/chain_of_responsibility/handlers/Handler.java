package ssad.chain_of_responsibility.handlers;

import ssad.chain_of_responsibility.Request;

public abstract class Handler {
    private Handler next;

    protected Handler(Handler next) {
        this.next = next; // setting of the next handler could be implemented via a special setNext() method
    }

    public void handleRequest(Request request) {
        if (next != null) {
            next.handleRequest(request);
        }
    }
}
