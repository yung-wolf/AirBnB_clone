#!/usr/bin/env python3

"""
Cmd line processor interpreter
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
                cls = storage.get_class(arg)
                new_obj = cls()
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
                cls = storage.get_class(args[0])
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
                cls_name = storage.get_class(args[0])
                cls_name = args[0]
                if len(args) < 2:
                    print('** instance id missing **')
                else:
                    obj_id = args[1]
                    objs = storage.all()
                    key = f"{str(cls_name)}.{obj_id}"
                    if key in objs:
                        del objs[key]
                        storage.save()
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
        lst = []  # an empty list
        objs = storage.all()
        if arg:  # print only arg inst (User/BaseModel)
            try:
                # check if arg is valid class name
                cls_name = storage.get_class(arg)
                if cls_name:
                    for k, v in objs.items():
                        cls, obj_id = k.split('.')
                        if cls == arg:
                            lst.append(f"{v}")
                    print(lst)
            except NameError:
                print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                lst.append(f"{v}")
            print(lst)

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
                    nm = args[2]  # attribute name
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
