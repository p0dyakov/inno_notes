package ssad.chain_of_responsibility.handlers;

import ssad.chain_of_responsibility.Request;

public class HandleSimpleRequest extends Handler {
    public HandleSimpleRequest(Handler next) {
        super(next);
    }

    @Override
    public void handleRequest(Request request) {
        if (request.getType() == Request.RequestType.SIMPLE) {
            System.out.println("Handling simple request\n");
        } else {
            System.out.print("Can't handle a request, assigning the next handler -> ");
            super.handleRequest(request);
        }
    }
}
