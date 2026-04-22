package ssad.observer.observers;

import ssad.observer.Observable;

public class CurrentConditionsDisplay implements Observer {
    private float temperature;
    private float humidity;
    private int pressure;

    public CurrentConditionsDisplay(Observable weatherData) {
        weatherData.registerObserver(this);
    }

    @Override
    public void update(float temperature, float humidity, int pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        display();
    }

    public void display() {
        System.out.printf("Current values: %.1f° and %.1f%% humidity. Pressure %d mm Hg.%n",
                temperature, humidity, pressure);
    }
}
