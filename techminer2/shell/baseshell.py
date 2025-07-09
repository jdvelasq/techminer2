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
        commands = [name[3:] for name in self.get_names() if name.startswith("do_")]
        commands = [command for command in commands if command not in ["help", "back"]]
        text = f"Commands: {' '.join(commands)}"
        self.intro = textwrap.fill(text, width=80, subsequent_indent=" " * 10) + "\n"

    def do_help(self, arg):
        """Help function."""
        if arg:
            try:
                func = getattr(self, f"help_{arg}")
                func()
            except AttributeError:
                print(f"No help available for '{arg}'")
        else:

            print("\nAvailable commands:\n")
            commands = [name[3:] for name in self.get_names() if name.startswith("do_")]
            commands = [
                command for command in commands if command not in ["help", "back"]
            ]
            for command in commands:
                print(f"  {command.ljust(15)} {getattr(self, f'do_{command}').__doc__}")
            print()
