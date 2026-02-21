from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.acronyms.general.commands import (
    execute_initialize_command,
)


class GeneralShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:acronyms:general")

    def do_initialize(self, arg):
        """Reset or create the thesaurus."""
        execute_initialize_command()
