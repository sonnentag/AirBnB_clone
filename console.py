#!/usr/bin/env python3
""" main """

import cmd


class HBNBCommand(cmd.Cmd):
    """ shell """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """ internal alias, same as do_quit """

        print()
        return True


if __name__ == "__main__":

    HBNBCommand().cmdloop()
