package ssad.observer.observers;

import ssad.observer.Observable;

public class HealthyConditionsMonitor implements Observer {
    private float temperature;
    private float humidity;
    private int pressure;

    public HealthyConditionsMonitor(Observable weatherData) {
        weatherData.registerObserver(this);
    }

    @Override
    public void update(float temperature, float humidity, int pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        reactToConditions();
    }

    public void reactToConditions() {
        final float MIN_TEMP = 16F;
        final float MAX_TEMP = 30F;

        if (temperature < MIN_TEMP) {
            System.out.println("Get dressed, it's cool outside");
        } else if (temperature > MAX_TEMP) {
            System.out.println("Take water and hat, it's too hot outside");
        }

        //TODO: think about other conditions
    }
}
