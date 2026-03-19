package ssad.singleton.zoo.problem;

public class MainSingleton {

    public static void main(String[] args) {
            AnimalZoo cat = new Cat();
            AnimalZoo duck = new Duck();
            cat.addToZoo();
            duck.addToZoo();
            // implementation of addToZoo() has to include both animals to the same Zoo instance
    }

}
