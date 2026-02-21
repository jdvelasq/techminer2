from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.descriptors.register.commands import (
    execute_acronyms_command,
    execute_initial_command,
    execute_keyword_command,
    execute_last_command,
)


class RegisterShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:register")

    def do_acronyms(self, arg):
        """Register acronyms as system known phrases."""
        execute_acronyms_command()

    def do_initial(self, arg):
        """Register new initial word."""
        execute_initial_command()

    def do_last(self, arg):
        """Register new last word."""
        execute_last_command()

    def do_keyword(self, arg):
        """Register new keyword."""
        execute_keyword_command()
