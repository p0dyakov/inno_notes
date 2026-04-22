package ssad.observer;

import ssad.observer.observers.Observer;

public interface Observable {
    void registerObserver(Observer observer); // subscribe()
    void removeObserver(Observer observer); // unsubscribe()
    void notifyObservers(); // notifySubscribers()
}