# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface for thesaurus descriptor operations."""


import readline
import rlcompleter  # type: ignore

from .base_shell import BaseShell
from .database.database_shell import DatabaseShell
from .thesaurus.thesaurus_shell import ThesaurusShell

readline.parse_and_bind("bind ^I rl_complete")


class MainShell(BaseShell):

    intro = "Welcome. Type help or ? to list commands.\n"

    prompt = "tm2 > "

    def do_database(self, arg):
        """Manage database operations."""
        DatabaseShell().cmdloop()
        self.do_help(arg)

    def do_thesaurus(self, arg):
        """Manage thesaurus operations."""
        ThesaurusShell().cmdloop()
        self.do_help(arg)
