package ssad.command.commands.air_humidifier_commands;

import ssad.command.commands.Command;
import ssad.command.devices.AirHumidifier;

public class SwitchOffAirHumidifier implements Command {
    private AirHumidifier airHumidifier;

    public SwitchOffAirHumidifier(AirHumidifier airHumidifier) {
        this.airHumidifier = airHumidifier;
    }

    @Override
    public void execute() {
        airHumidifier.turnOff();
    }

    @Override
    public void undo() {
        airHumidifier.turnOn();
        //TODO state of mode is not stored
        airHumidifier.setMode(AirHumidifier.AirHumidifierModes.SLOW);
    }
}
