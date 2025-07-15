# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import cmd

from colorama import Fore, Style, init

init(autoreset=True)


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

            print(f"\n{Fore.LIGHTBLACK_EX}Commands:{Style.RESET_ALL}\n")
            commands = [name[3:] for name in self.get_names() if name.startswith("do_")]
            commands = [
                command
                for command in commands
                if command not in ["help", "back", "q", "quit", "exit", "Q"]
            ]
            for command in commands:
                print(
                    f"  {command.ljust(15)} {Fore.LIGHTBLACK_EX}{getattr(self, f'do_{command}').__doc__}{Style.RESET_ALL}"
                )
            print()

    def do_q(self, arg):
        """Go back or exit."""
        print()
        return True

    def do_Q(self, arg):
        """Go back or exit."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        self.do_help(None)

    def default(self, line):
        """Handle unknown commands."""
        print()
        print(f"*** Unknown command: <{line}>.")
        self.do_help(None)
