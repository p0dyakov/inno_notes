package ssad.command.commands.light_commands;

import ssad.command.commands.Command;
import ssad.command.devices.Light;

public class SwitchOnLight implements Command {
    private Light light;

    public SwitchOnLight(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.turnOn();
    }

    @Override
    public void undo() {
        light.turnOff();
    }
}
