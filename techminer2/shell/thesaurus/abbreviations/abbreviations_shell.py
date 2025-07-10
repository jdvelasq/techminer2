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


class AbbreviationsShell(BaseShell):

    prompt = "tm2 > thesaurus > abbreviations > "

    def do_general(self, arg):
        """General commands."""
        GeneralShell().cmdloop()
        self.do_help(arg)
