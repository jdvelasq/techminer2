# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface for the Thesaurus subsystem."""

import cmd
import readline
import rlcompleter  # type: ignore

from ....baseshell import BaseShell
from .commands.dataframe import execute_dataframe_command

readline.parse_and_bind("bind ^I rl_complete")


class GeneralShell(BaseShell):

    prompt = "tm2 > database > metrics > general > "

    def do_dataframe(self, arg):
        """Prints the dataset general metrics."""
        execute_dataframe_command()

    def do_back(self, arg):
        """Exit the CLI."""
        return True


if __name__ == "__main__":
    GeneralShell().cmdloop()
