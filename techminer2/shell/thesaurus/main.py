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
from .descriptors.main import DescriptorsCLI

readline.parse_and_bind("bind ^I rl_complete")


class ThesaurusShell(BaseShell):

    prompt = "tm2 > thesaurus > "

    # Main menu commands
    # def do_abbreviations(self, arg):
    #     """Abbreviations-related commands."""
    #     print("Entering abbreviations menu...")
    #     AbbreviationsCLI().cmdloop()

    # def do_countries(self, arg):
    #     """Countries-related commands."""
    #     print("Entering countries menu...")
    #     CountriesCLI().cmdloop()

    def do_descriptors(self, arg):
        """Commands for manipulating descriptors.the.txt thesaurus file."""
        DescriptorsCLI().cmdloop()

    # def do_organizations(self, arg):
    #     """Organizations-related commands."""
    #     print("Entering organizations menu...")
    #     OrganizationsCLI().cmdloop()

    # def do_references(self, arg):
    #     """References-related commands."""
    #     print("Entering references menu...")
    #     ReferencesCLI().cmdloop()

    def do_back(self, arg):
        """Exit the CLI."""
        return True


if __name__ == "__main__":
    ThesaurusShell().cmdloop()
