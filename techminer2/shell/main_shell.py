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

from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.database.database_shell import DatabaseShell
from techminer2.shell.thesaurus.thesaurus_shell import ThesaurusShell
from techminer2.shell.zotero.zotero_shell import ZoteroShell
from techminer2.shell.package.package_shell import PackageShell

readline.parse_and_bind("bind ^I rl_complete")


class MainShell(BaseShell):

    intro = "Welcome. Type help or ? to list commands.\n"

    prompt = make_colorized_prompt("tm2")

    def do_database(self, arg):
        """Manage database operations."""
        DatabaseShell().cmdloop()
        self.do_help(arg)

    def do_thesaurus(self, arg):
        """Manage thesaurus operations."""
        ThesaurusShell().cmdloop()
        self.do_help(arg)

    def do_package(self, arg):
        """Manage package operations."""
        PackageShell().cmdloop()
        self.do_help(arg)

    def do_zotero(self, arg):
        """Manage Zotero operations."""
        ZoteroShell().cmdloop()
        self.do_help(arg)
