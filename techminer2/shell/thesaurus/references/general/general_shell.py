from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.references.general.commands import (
    execute_apply_command,
    execute_initialize_command,
    execute_integrity_command,
)


class GeneralShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:references:general")

    def do_apply(self, arg):
        """Apply the thesaurus."""
        execute_apply_command()

    def do_initialize(self, arg):
        """Reset or create the thesaurus."""
        execute_initialize_command()

    def do_integrity(self, arg):
        """Verify thesaurus integrity."""
        execute_integrity_command()
