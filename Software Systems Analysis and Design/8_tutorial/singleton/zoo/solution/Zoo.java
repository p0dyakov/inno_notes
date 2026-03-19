package ssad.singleton.zoo.solution;

import java.util.ArrayList;
import java.util.List;

public class Zoo {

    private final List<AnimalZoo> animalList;

    private static Zoo instance; // lazy initialization
    public static int getInstanceCounter = 0;
    public static int constructorCounter = 0;

    public static Zoo getInstance() {
        if (instance == null) {
            instance = new Zoo();
        }
        System.out.println("getInstanceCounter=" + ++getInstanceCounter);
        return instance;
    }

    private Zoo() {
        this.animalList = new ArrayList<>();
        System.out.println("constructorCounter=" + ++constructorCounter);
    }

    public void addAnimal(AnimalZoo animal) {
        animalList.add(animal);
    }

    public void displayAnimals() {
        System.out.printf("We have %d Animals in the zoo %n", animalList.size());
        System.out.println("All animals must entertain:");
        animalList.forEach(AnimalZoo::entertain);
    }
}
