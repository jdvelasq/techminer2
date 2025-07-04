# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface for thesaurus descriptor operations."""


import cmd
import readline
import rlcompleter  # type: ignore

from ..basecli import BaseCLI
from .descriptors.shell import DescriptorsCLI

readline.parse_and_bind("bind ^I rl_complete")


class MainShell(BaseCLI):
    intro = "Welcome. Type help or ? to list commands.\n"
    prompt = "tm2 > "

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

    def do_exit(self, arg):
        """Exit the CLI."""
        return True

    def do_back(self, arg):
        """Exit the CLI."""
        return True

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
            for command in self.get_names():
                if command.startswith("do_"):
                    print(f"  {command[3:].ljust(15)} {getattr(self, command).__doc__}")
            print()


if __name__ == "__main__":
    MainShell().cmdloop()
