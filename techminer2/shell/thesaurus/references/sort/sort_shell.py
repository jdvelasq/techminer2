from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.references.sort.commands import (
    execute_alphabet_command,
    execute_fuzzy_command,
    execute_match_command,
)


class SortShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:references:sort")

    def do_alphabet(self, arg):
        """Sort keys alphabetically."""
        execute_alphabet_command()

    def do_fuzzy(self, arg):
        """Sort keys by fuzzy match."""
        execute_fuzzy_command()

    def do_match(self, arg):
        """Sort keys by pattern match."""
        execute_match_command()
