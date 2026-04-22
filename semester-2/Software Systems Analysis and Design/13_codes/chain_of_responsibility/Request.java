package ssad.chain_of_responsibility;

public class Request {
    private RequestType type;

    public Request(RequestType type) {
        this.type = type;
    }

    public RequestType getType() {
        return type;
    }

    public enum RequestType {
        SIMPLE,
        MEDIUM,
        COMPLEX
    }
}

