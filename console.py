#!/usr/bin/python3
"""
Command interpreter for Alx AirBnB project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import storage, CNT
import shlex


classes = storage.CNT.keys()

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
        print('+----------------------------+')
        print('|    Welcome to hbnb CLI!    |')
        print('|   for help, input \'help\'   |')
        print('|   for quit, input \'quit\'   |')
        print('+----------------------------+')

    def postloop(self):
        """
        handles exit to command interpreter
        """
        print('+----------------------------+')
        print('|  Sure you enjoyed trying!  |')
        print('+----------------------------+')

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

    def do_quit(self, line):
        """quit: quit
        USAGE: Command to quit the program
        """
        exit()

    def do_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

    def do_create(self, args):
        """
        creates new instance of a class
        example: ($ create ClassName)
        prints an error message if name is missing or does not exist
        """
        args, n = parse(args)

        if not n:
            print("{}".format(HBNBCommand.ERR[0]))
        elif args[0] not in classes:
            print("{}".format(HBNBCommand.ERR[1]))
        elif n == 1:
            obj = eval(args[0])()
            print(obj.id)
            obj.save()
        else:
            print("** Too many argument for create **")
            pass
    def do_show(self, args):
        """prints the the dict representation of the instance
            example: ($ show BaseModel 1234-1234-1234)
        """
        if args:
            args, length = parse(args)
            if length < 2:
                if length < 1:
                    print("{}".format(HBNBCommand.ERR[0]))
                elif length == 1:
                    if args[0] not in classes:
                        print("{}".format(HBNBCommand.ERR[1]))
                        return
                    print("** instance id missing **")
            else:
                all_objs = storage.all()
                key = args[0] + '.' + args[1]
                print(all_objs[key])

def parse(line):
        """split the line arguments by spaces"""
        args = shlex.split(line)
        return args, len(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
