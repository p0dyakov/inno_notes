package ssad.command.devices;

public class Light {
    private boolean enabled;

    public void turnOn() {
        if (!enabled) {
            enabled = true;
            System.out.println("Turning the light on");
        } else {
            System.err.println("Impossible to turn the light on");
        }
    }

    public void turnOff() {
        if (enabled) {
            enabled = false;
            System.out.println("Turning the light off");
        } else {
            System.err.println("Impossible to turn the light off");
        }
    }

    public boolean isEnabled() {
        return enabled;
    }
}
