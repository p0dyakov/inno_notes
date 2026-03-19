package ssad.singleton.zoo.problem;

import java.util.ArrayList;
import java.util.List;

public class Zoo {

    private List<AnimalZoo> animalList;

    // it will run as many times as you initialize an object
    public Zoo() {
        animalList = new ArrayList<>();
    }

    public void addAnimal(AnimalZoo animal) {
        animalList.add(animal);
    }

    public void displayAnimals() {
        System.out.printf("We have %d animals in the zoo %n", animalList.size());
        System.out.println("All animals must entertain:");
        animalList.forEach(AnimalZoo::entertain);
    }
}
