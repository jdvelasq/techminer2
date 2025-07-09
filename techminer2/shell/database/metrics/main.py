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
from .general.main import GeneralShell

readline.parse_and_bind("bind ^I rl_complete")


class MetricsShell(BaseShell):

    prompt = "tm2 > database > ingest > metrics >"

    def do_general(self, arg):
        """General metrics."""
        GeneralShell().cmdloop()

    def do_back(self, arg):
        """Exit the CLI."""
        return True


if __name__ == "__main__":
    MetricsShell().cmdloop()
