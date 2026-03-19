package ssad.singleton.zoo.solution;

public abstract class AnimalZoo {

    public abstract void entertain();

    public void addToZoo() {
        Zoo zoo = Zoo.getInstance();
        zoo.addAnimal(this);
    }
}
