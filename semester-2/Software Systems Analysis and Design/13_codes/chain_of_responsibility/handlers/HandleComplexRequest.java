package ssad.chain_of_responsibility.handlers;

import ssad.chain_of_responsibility.Request;

public class HandleComplexRequest extends Handler {
    public HandleComplexRequest(Handler next) {
        super(next);
    }

    @Override
    public void handleRequest(Request request) {
        if (request.getType() == Request.RequestType.COMPLEX ||
                request.getType() == Request.RequestType.MEDIUM ||
                request.getType() == Request.RequestType.SIMPLE) {
            System.out.println("Handling complex request\n");
        } else {
            // Ideally not to have unhandleable requests
            System.out.print("Can't handle a request, the level of complexity is null"); // assigning the next handler -> ");
//            super.handleRequest(request);
        }
    }
}
