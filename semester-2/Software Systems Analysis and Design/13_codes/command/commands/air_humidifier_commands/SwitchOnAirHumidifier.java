package ssad.command.commands.air_humidifier_commands;

import ssad.command.commands.Command;
import ssad.command.devices.AirHumidifier;

public class SwitchOnAirHumidifier implements Command {
    private AirHumidifier airHumidifier;

    public SwitchOnAirHumidifier(AirHumidifier airHumidifier) {
        this.airHumidifier = airHumidifier;
    }

    @Override
    public void execute() {
        airHumidifier.turnOn();
        airHumidifier.setMode(AirHumidifier.AirHumidifierModes.SLOW);
    }

    @Override
    public void undo() {
        airHumidifier.turnOff();
    }
}
