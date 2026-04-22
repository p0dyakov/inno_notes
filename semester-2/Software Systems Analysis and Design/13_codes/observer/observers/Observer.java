package ssad.observer.observers;

public interface Observer {
    void update(float temperature, float humidity, int pressure);
}
