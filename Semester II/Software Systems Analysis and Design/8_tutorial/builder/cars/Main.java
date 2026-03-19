package ssad.builder.cars;

public class Main {
    public static void main(String[] args) {
        CarBuilder builder = new SportsCarBuilder();
//        CarBuilder builder = new ClassicCarBuilder(); // another car option
        AutomotiveEngineer engineer = new AutomotiveEngineer(builder);
        Car car = engineer.manufactureCar();
        if (car != null) {
            System.out.println("Below car delivered: ");
            System.out.println("============================================================================");
            System.out.println(car);
            System.out.println("============================================================================");
        } else {
            System.out.println("Problems with current producing");
        }
    }
}
