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

from ..baseshell import BaseShell
from .ingest.main import IngestShell

readline.parse_and_bind("bind ^I rl_complete")


class DatabaseShell(BaseShell):

    prompt = "tm2 > database > "

    def do_ingest(self, arg):
        """Commands for raw data ingestion."""
        IngestShell().cmdloop()

    def do_back(self, arg):
        """Return to the previous menu."""
        return True


if __name__ == "__main__":
    DatabaseShell().cmdloop()
