# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface."""

from ...baseshell import BaseShell
from .general.main import GeneralCLI
from .remove.main import RemoveCLI
from .translate.main import TranslateCLI


class DescriptorsCLI(BaseShell):

    prompt = "tm2 > thesaurus > descriptors > "

    def do_general(self, arg):
        """General commands"""
        GeneralCLI().cmdloop()
        self.do_help(arg)

    def do_remove(self, arg):
        RemoveCLI().cmdloop()
        self.do_help(arg)

    # def do_replace(self, arg):
    #     ReplaceCLI().cmdloop()

    # def do_sort(self, arg):
    #     SortCLI().cmdloop()

    def do_translate(self, arg):
        """Convert between American and British spelling."""
        TranslateCLI().cmdloop()
        self.do_help(arg)
