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
from .general import GeneralCLI
from .remove import RemoveCLI
from .translate import TranslateCLI


class DescriptorsCLI(BaseShell):

    prompt = "tm2 > descriptors > "

    def do_general(self, arg):
        """General commands"""
        GeneralCLI().cmdloop()

    def do_remove(self, arg):
        RemoveCLI().cmdloop()

    # def do_replace(self, arg):
    #     ReplaceCLI().cmdloop()

    # def do_sort(self, arg):
    #     SortCLI().cmdloop()

    def do_translate(self, arg):
        TranslateCLI().cmdloop()

    def do_back(self, arg):
        """Return a menu level."""
        return True
