package ssad.singleton.zoo.solution;


public class MainSingleton {

    public static void main(String[] args) {
        AnimalZoo cat = new Cat();
        cat.addToZoo();
        AnimalZoo duck = new Duck();
        duck.addToZoo();
        Zoo zoo = Zoo.getInstance();
        zoo.displayAnimals();
    }

}
