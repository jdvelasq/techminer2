from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.references.general.general_shell import GeneralShell
from techminer2.shell.thesaurus.references.sort.sort_shell import SortShell


class ReferencesShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:references")

    def do_general(self, arg):
        """General thesaurus operations."""
        GeneralShell().cmdloop()
        self.do_help(arg)

    def do_sort(self, arg):
        """Sort the thesaurus."""
        SortShell().cmdloop()
        self.do_help(arg)
