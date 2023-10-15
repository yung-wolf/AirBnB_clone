#!/usr/bin/env python3

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of class BaseModel,
        saves it, and prints the id.
        """
        if arg:
            try:
                new_obj = BaseModel()
                new_obj.save()
                print(new_obj.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        """
        if arg:
            try:
                args = arg.split()
                cls_name = args[0]
                if len(args) < 2:
                    print('** instance id missing **')
                else:
                    obj_id = args[1]
                    objs = storage.all()
                    key = f"{cls_name}.{obj_id}"
                    if key in objs:
                        print(objs[key])
                    else:
                        print('** no instance found **')
            except NameError:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

           Save changes into the JSON file.
        """
        if arg:
            try:
                args = arg.split()
                cls_name = args[0]
                if len(args) < 2:
                    print('** instance id missing **')
                else:
                    obj_id = args[1]
                    objs = storage.all()
                    key = f"{cls_name}.{obj_id}"
                    if key in objs:
                        del objs[key]
                    else:
                        print('** no instance found **')
            except NameError:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def emptyline(self):
        """Called when an empty line is entered"""

    def do_quit(self, line):
        """Quits cmd interpreter"""
        sys.exit()

    def do_EOF(self, line):
        """end of file"""
        return True

    def postloop(self):
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
