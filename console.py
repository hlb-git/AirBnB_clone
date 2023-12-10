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
        print('|   For help, input \'help\'   |')
        print('|    To quit, input \'quit\'   |')
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
        print("    _     _  _ _||\\ |/  \\ | _  _  _|_|_     _  _ _| ")
        print("|_||_)\\)/(_|| (_|| \\|\\__/ || )(_)| |_| )\\)/(_|| (_| ")
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
        return True

    def do_EOF(self, line):
        """function to handle EOF"""
        print("")
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
                if "{}.{}".format(args[0], args[1]) not in all_objs.keys():
                    print("** no instance found **")
                else:
                    key = args[0] + '.' + args[1]
                    print(all_objs[key])

    def do_destroy(self, args):
        """deletes a class instance of a given id"""
        args, n = parse(args)

        all_objects = storage.all()
        if not n:
            print("{}".format(HBNBCommand.ERR[0]))
        elif args[0] not in classes:
            print("{}".format(HBNBCommand.ERR[1]))
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_objects.keys():
            print("** no instance found **")
        else:
            del all_objects["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """print all the instance of a class provided as argument"""
        args, length = parse(args)

        if length > 0 and args[0] not in classes:
            print("{}".format(HBNBCommand.ERR[1]))
        else:
            objects_list = []
            for instance in storage.all().values():
                if length > 0 and args[0] == instance.__class__.__name__:
                    objects_list.append(instance.__str__())
                elif length == 0:
                    objects_list.append(instance.__str__())
            print(objects_list)

    def do_update(self, args):
        """update attribute of an instance
            example: ($ update <ModelName> <model id> <attribute> <value>)
        """
        args, length = parse(args)
        all_objects = storage.all()

        if not length:
            print("{}".format(HBNBCommand.ERR[0]))
        elif args[0] not in classes:
            print("{}".format(HBNBCommand.ERR[1]))
        if length == 1:
            print("** instance id missing **")
        if "{}.{}".format(args[0], args[1]) not in all_objects.keys():
            print("** no instance found **")
        if length == 2:
            print("** attribute name missing **")
        if length == 3:
            print("** value missing **")

        if length == 4:
            obj = all_objects["{}.{}".format(args[0], args[1])]
        if args[2] in obj.__class__.__dict__.keys():
            value_type = type(obj.__class__.__dict__[args[2]])
            obj.__dict__[args[2]] = value_type(args[3])
        else:
            obj.__dict__[args[2]] = args[3]


def parse(line):
    """split the line arguments by spaces"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
