package ssad.builder.cars;

public interface CarBuilder {

    // Stage 1
    CarBuilder fixChassis();

    // Stage 2
    CarBuilder fixBody();

    // Stage 3
    CarBuilder paint();

    // Stage 4
    CarBuilder fixInterior();

    // Car production
    Car build();
}
