from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.acronyms.register.commands import (
    execute_phrases_command,
)


class RegisterShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:acronyms:register")

    def do_phrases(self, arg):
        """Register new noun phrases in the system."""
        execute_phrases_command()
