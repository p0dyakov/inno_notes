package ssad.command;

import ssad.command.commands.Command;

public class RemoteControl {
    private Command commandSwitchOn;
    private Command commandSwitchOff;
    private Command undoCommand;

    //TODO add air humidifier commands

    public void setCommand(Command commandSwitchOn, Command commandSwitchOff) {
        this.commandSwitchOn = commandSwitchOn;
        this.commandSwitchOff = commandSwitchOff;
    }

    public void pressSwitchOnButton() {
        if (commandSwitchOn != null) {
            commandSwitchOn.execute();
            undoCommand = commandSwitchOff;
        } else {
            System.err.println("Null pointer to Switch On command");
        }
    }

    public void pressSwitchOffButton() {
        if (commandSwitchOff != null) {
            commandSwitchOff.execute();
            undoCommand = commandSwitchOn;
        } else {
            System.err.println("Null pointer to Switch Off command");
        }
    }

    public void undoCommand() {
        if (undoCommand != null) {
            undoCommand.execute();
        } else {
            System.err.println("Null pointer to Undo command");
        }
    }
}
