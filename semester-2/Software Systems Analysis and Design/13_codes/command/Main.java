package ssad.command;

import ssad.command.commands.air_humidifier_commands.SwitchOffAirHumidifier;
import ssad.command.commands.light_commands.SwitchOffLight;
import ssad.command.commands.air_humidifier_commands.SwitchOnAirHumidifier;
import ssad.command.commands.light_commands.SwitchOnLight;
import ssad.command.devices.AirHumidifier;
import ssad.command.devices.Light;

public class Main {

    public static void main(String[] args) {
        Light light = new Light();
        RemoteControl remoteControl = new RemoteControl();
        remoteControl.setCommand(new SwitchOnLight(light), new SwitchOffLight(light));
        remoteControl.pressSwitchOnButton();
        remoteControl.pressSwitchOffButton();
        remoteControl.undoCommand();
//        remoteControl.undoCommand();

        System.out.println();

        AirHumidifier airHumidifier = new AirHumidifier();
        remoteControl.setCommand(new SwitchOnAirHumidifier(airHumidifier), new SwitchOffAirHumidifier(airHumidifier));
        remoteControl.pressSwitchOnButton();
        remoteControl.pressSwitchOffButton();
        remoteControl.undoCommand();
//        remoteControl.undoCommand();
    }
}
