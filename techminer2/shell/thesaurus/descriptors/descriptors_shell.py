from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.descriptors.clean.clean_shell import CleanShell
from techminer2.shell.thesaurus.descriptors.general.general_shell import GeneralShell
from techminer2.shell.thesaurus.descriptors.register.register_shell import RegisterShell
from techminer2.shell.thesaurus.descriptors.remove.remove_shell import RemoveShell
from techminer2.shell.thesaurus.descriptors.replace.replace_shell import ReplaceShell
from techminer2.shell.thesaurus.descriptors.sort.sort_shell import SortShell
from techminer2.shell.thesaurus.descriptors.translate.translate_shell import (
    TranslateShell,
)


class DescriptorsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors")

    def do_clean(self, arg):
        """Clean commands."""
        CleanShell().cmdloop()
        self.do_help(arg)

    def do_general(self, arg):
        """General thesaurus operations."""
        GeneralShell().cmdloop()
        self.do_help(arg)

    def do_remove(self, arg):
        """Remove words from the thesaurus."""
        RemoveShell().cmdloop()
        self.do_help(arg)

    def do_register(self, arg):
        """Register new terms in the system."""
        RegisterShell().cmdloop()
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
