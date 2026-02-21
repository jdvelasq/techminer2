from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.acronyms.general.general_shell import GeneralShell
from techminer2.shell.thesaurus.acronyms.register.register_shell import RegisterShell


class AcronymsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:acronyms")

    def do_general(self, arg):
        """General commands."""
        GeneralShell().cmdloop()
        self.do_help(arg)

    def do_register(self, arg):
        """Register new noun phrases in the system."""
        RegisterShell().cmdloop()
        self.do_help(arg)
