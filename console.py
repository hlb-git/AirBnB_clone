#!/usr/bin/python3
"""
Command interpreter for Alx AirBnB project
"""
import cmd
from models import storage, CNT


class HBNBCommand(cmd.Cmd):
    """
    Command inerpreter class
    """
    prompt = '(hbnb) '
    ERR = [
        '** class name missing **',
        '** class doesn\'t exist **',
        '** instance id missing **',
        '** no instance found **',
        '** attribute name missing **',
        '** value missing **',
        ]
    def preloop(self):
        """
        handles intro to command interpreter
        """
        print('.----------------------------.')
        print('|    Welcome to hbnb CLI!    |')
        print('|   for help, input \'help\'   |')
        print('|   for quit, input \'quit\'   |')
        print('.----------------------------.')

    def postloop(self):
        """
        handles exit to command interpreter
        """
        print('.----------------------------.')
        print('|  Sure you enjoyed trying!  |')
        print('.----------------------------.')

    def default(self, line):
        """
        default response for unknown commands
        """
        print("This \"{}\" is invalid, run \"help\" "
              "for more explanations".format(line))

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def __class_err(self, arg):
        """
        private: checks for missing class or unknown class
        """
        error = 0
        if len(arg) == 0:
            print(HBNBCommand.ERR[0])
            error = 1
        else:
            if isinstance(arg, list):
                arg = arg[0]
            if arg not in CNT.keys():
                print(HBNBCommand.ERR[1])
                error = 1
        return error

    def __id_err(self, arg):
        """
        private checks for missing ID or unknown ID
        """
        error = 0
        if (len(arg) < 2):
            error += 1
            print(HBNBCommand.ERR[2])
        if not error:
            storage_objs = storage.all()
            for key, value in storage_objs.items():
                temp_id = key.split('.')[1]
                if temp_id == arg[1] and arg[0] in key:
                    return error
            error += 1
            print(HBNBCommand.ERR[3])
        return error

    def LH_airbnb(self, arg):
        """airbnb: airbnb
        SYNOPSIS: Command changes prompt string"""
        print("                      __ ___                        ")
        print("    _     _  _ _||\ |/  \ | _  _  _|_|_     _  _ _| ")
        print("|_||_)\)/(_|| (_|| \|\__/ || )(_)| |_| )\)/(_|| (_| ")
        print("   |                                                ")
        if HBNBCommand.prompt == '(hbnb) ':
            HBNBCommand.prompt = " /_ /_ _  /_\n/ //_// //_/ "
        else:
            HBNBCommand.prompt = '(hbnb) '
        arg = arg.split()
        error = self.__class_err(arg)

    def LH_quit(self, line):
        """quit: quit
        USAGE: Command to quit the program
        """
        return True

    def LH_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
