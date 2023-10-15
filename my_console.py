#!/usr/bin/env python3

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Simple command processor example"""

    prompt = "(hbnb) "

    FRIENDS = ['Alice', 'Adam', 'Barbara', 'Bob']

    def do_greet(self, person):
        if person and person in self.FRIENDS:
            print("hi, %s!" % person)
        elif person:
            print("hello, " + person)
        else:
            print("hello")

    def help_greet(self):
        print('\n' + "Greet [person]",
                     "\nGreet the named person")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)

                            ]
        return completions

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

