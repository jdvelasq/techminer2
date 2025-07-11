# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....base_shell import BaseShell
from .commands import (
    execute_alphabet_command,
    execute_endswith_command,
    execute_exact_command,
    execute_fuzzy_command,
    execute_keylength_command,
    execute_match_command,
    execute_startswith_command,
    execute_wordlength_command,
    execute_wordmatch_command,
)


class SortShell(BaseShell):

    prompt = "tm2 > thesaurus > organizations > sort > "

    def do_alphabet(self, arg):
        """Sort keys alphabetically."""
        execute_alphabet_command()

    def do_endswith(self, arg):
        """Sort keys by ending pattern."""
        execute_endswith_command()

    def do_exact(self, arg):
        """Sort keys by exact match."""
        execute_exact_command()

    def do_fuzzy(self, arg):
        """Sort keys by fuzzy match."""
        execute_fuzzy_command()

    def do_keylength(self, arg):
        """Sort keys by key length."""
        execute_keylength_command()

    def do_match(self, arg):
        """Sort keys by pattern match."""
        execute_match_command()

    def do_startswith(self, arg):
        """Sort keys by starting pattern."""
        execute_startswith_command()

    def do_wordlength(self, arg):
        """Sort keys by word length."""
        execute_wordlength_command()

    def do_wordmatch(self, arg):
        """Sort keys by word match."""
        execute_wordmatch_command()
