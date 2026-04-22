package ssad.observer;

import ssad.observer.observers.CurrentConditionsDisplay;
import ssad.observer.observers.Observer;

public class WeatherStation {
    // TODO: add more observers
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        Observer currentDisplay = new CurrentConditionsDisplay(weatherData);

        weatherData.setMeasurements(29f, 65f, 745);
        weatherData.setMeasurements(39f, 70f, 760);
        weatherData.setMeasurements(42f, 72f, 763);
        weatherData.removeObserver(currentDisplay);
        weatherData.setMeasurements(0f, 15f, 763);
    }
}
