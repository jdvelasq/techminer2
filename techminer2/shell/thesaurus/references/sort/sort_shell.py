# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....base_shell import BaseShell
from ....colorized_prompt import make_colorized_prompt
from .commands import (execute_alphabet_command, execute_fuzzy_command,
                       execute_match_command)


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
