package ssad.command.commands.light_commands;

import ssad.command.commands.Command;
import ssad.command.devices.Light;

public class SwitchOffLight implements Command {
    private Light light;

    public SwitchOffLight(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.turnOff();
    }

    @Override
    public void undo() {
        light.turnOn();
    }
}
