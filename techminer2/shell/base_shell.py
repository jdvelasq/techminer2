# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import cmd
import textwrap


class BaseShell(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.intro = ""
        self.do_help(None)  # Print help on startup

    def do_help(self, arg):
        """Help function."""
        if arg:
            try:
                func = getattr(self, f"help_{arg}")
                func()
            except AttributeError:
                print(f"No help available for '{arg}'")
        else:

            print("\nCommands:\n")
            commands = [name[3:] for name in self.get_names() if name.startswith("do_")]
            commands = [
                command
                for command in commands
                if command not in ["help", "back", "q", "quit", "exit"]
            ]
            for command in commands:
                print(f"  {command.ljust(15)} {getattr(self, f'do_{command}').__doc__}")
            print()

    def do_q(self, arg):
        """Go back or exit."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        self.do_help(None)
