package ssad.chain_of_responsibility;

import ssad.chain_of_responsibility.handlers.HandleSimpleRequest;
import ssad.chain_of_responsibility.handlers.HandleMediumRequest;
import ssad.chain_of_responsibility.handlers.HandleComplexRequest;
import ssad.chain_of_responsibility.handlers.Handler;

public class Main {

    //TODO: update so that tasks are always attempted to be be handled by simple handlers
    public static void main(String[] args) {
        Handler complexTaskHandler = new HandleComplexRequest(null);
        Handler mediumTaskHandler = new HandleMediumRequest(complexTaskHandler);
        Handler simpleTaskHandler = new HandleSimpleRequest(mediumTaskHandler);

        Request simpleRequest = new Request(Request.RequestType.SIMPLE);
        Request mediumRequest = new Request(Request.RequestType.MEDIUM);
        Request complexRequest = new Request(Request.RequestType.COMPLEX);

        simpleTaskHandler.handleRequest(simpleRequest);
        simpleTaskHandler.handleRequest(mediumRequest);
        simpleTaskHandler.handleRequest(complexRequest);

        simpleTaskHandler.handleRequest(mediumRequest);
        mediumTaskHandler.handleRequest(mediumRequest);
        simpleTaskHandler.handleRequest(simpleRequest);
        simpleTaskHandler.handleRequest(complexRequest);
        complexTaskHandler.handleRequest(complexRequest);
        complexTaskHandler.handleRequest(simpleRequest);
    }
}
