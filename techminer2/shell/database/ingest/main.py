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

from ...baseshell import BaseShell
from .commands.scopus import execute_scopus_command

readline.parse_and_bind("bind ^I rl_complete")


class IngestShell(BaseShell):

    prompt = "tm2 > database > ingest > "

    def do_scopus(self, arg):
        """Import Scopus raw data."""
        execute_scopus_command()

    def do_back(self, arg):
        """Exit the CLI."""
        return True


if __name__ == "__main__":
    IngestShell().cmdloop()
