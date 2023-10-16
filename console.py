#!/usr/bin/env python3

"""
Cmd line processor
"""

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

    def do_all(self, arg=""):
        """Prints all string representation of all instances.
        class name is optional.

        Ex: $ all BaseModel or $ all
        """
        if arg == "" or arg == "BaseModel":
            objs = storage.all()
            lst = []  # an empty list
            for k, v in objs.items():
                lst.append(f"{v}")
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'
        """
        if arg:
            try:
                args = arg.split()
                cls_name = args[0]
                cls = storage.get_class(cls_name)
                if len(args) < 2:
                    if not cls:
                        print("** class doesn't exist **")
                    else:
                        print('** instance id missing **')
                elif len(args) < 3:
                    obj_id = args[1]
                    objs = storage.all()
                    key = f"{cls_name}.{obj_id}"
                    if key in objs:
                        print('** attribute name missing **')
                    else:
                        print('** no instance found **')
                else:
                    obj_id = args[1]
                    nm = args[2]
                    objs = storage.all()
                    # check class name is valid
                    key = f"{cls_name}.{obj_id}"
                    if key in objs:
                        if nm in objs[key].__dict__:
                            objs[key].__dict__[nm] = args[3].replace('"', '')
                            storage.save()
                        else:
                            print("** value missing **")
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
