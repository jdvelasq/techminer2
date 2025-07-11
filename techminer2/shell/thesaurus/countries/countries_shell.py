# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ...base_shell import BaseShell
from .general.general_shell import GeneralShell
from .sort.sort_shell import SortShell


class CountriesShell(BaseShell):

    prompt = "tm2 > thesaurus > countries > "

    def do_general(self, arg):
        """General thesaurus operations."""
        GeneralShell().cmdloop()
        self.do_help(arg)

    def do_sort(self, arg):
        """Sort the thesaurus by different criteria."""
        SortShell().cmdloop()
        self.do_help(arg)
