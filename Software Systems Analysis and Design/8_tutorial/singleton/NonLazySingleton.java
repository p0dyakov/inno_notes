package ssad.singleton;

// better to avoid this implementation
public class NonLazySingleton {
    private static final NonLazySingleton unique = new NonLazySingleton();

    private NonLazySingleton() { }

    public static NonLazySingleton getInstance() {
        return unique;
    }
}