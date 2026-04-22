package ssad.command.devices;

public class AirHumidifier {
    private boolean enabled;
    private AirHumidifierModes mode;

    public void turnOn() {
        if (!enabled) {
            enabled = true;
            mode = AirHumidifierModes.SLOW;
            System.out.println("Turning the air humidifier on");
        } else {
            System.err.println("Impossible to turn the humidifier on");
        }
    }

    public void turnOff() {
        if (enabled) {
            enabled = false;
            System.out.println("Turning the air humidifier off");
        } else {
            System.err.println("Impossible to turn the humidifier off");
        }
    }

    public void setMode(AirHumidifierModes mode) {
        this.mode = mode;
    }

    public boolean isEnabled() {
        return enabled;
    }

    public enum AirHumidifierModes {
        SLOW,
        MEDIUM,
        HIGH
    }
}
