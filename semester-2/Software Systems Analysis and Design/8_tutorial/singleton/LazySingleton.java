package ssad.singleton;

public class LazySingleton {
    private static LazySingleton unique;

    private LazySingleton() { }

    public static LazySingleton getInstance() {
        if (unique == null) {
            unique = new LazySingleton(); // lazy initialization
        }
        return unique;
    }
}