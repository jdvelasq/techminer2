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
from .remove.remove_shell import RemoveShell
from .replace.replace_shell import ReplaceShell
from .sort.sort_shell import SortShell
from .translate.translate_shell import TranslateShell


class DescriptorsShell(BaseShell):

    prompt = "tm2 > thesaurus > descriptors > "

    def do_general(self, arg):
        """General thesaurus operations."""
        GeneralShell().cmdloop()
        self.do_help(arg)

    def do_remove(self, arg):
        """Remove words from the thesaurus."""
        RemoveShell().cmdloop()
        self.do_help(arg)

    def do_replace(self, arg):
        """Replace words in the thesaurus."""
        ReplaceShell().cmdloop()
        self.do_help(arg)

    def do_sort(self, arg):
        """Sort the thesaurus."""
        SortShell().cmdloop()
        self.do_help(arg)

    def do_translate(self, arg):
        """Translate American and British spelling."""
        TranslateShell().cmdloop()
        self.do_help(arg)
