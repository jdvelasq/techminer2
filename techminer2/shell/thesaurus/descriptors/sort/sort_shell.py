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
    execute_occurrences_command,
    execute_startswith_command,
    execute_wordlength_command,
    execute_wordmatch_command,
)


class SortShell(BaseShell):

    prompt = "tm2 > thesaurus > descriptors > sort > "

    def do_alphabet(self, arg):

        execute_alphabet_command()

    def do_endswith(self, arg):

        execute_endswith_command()

    def do_exact(self, arg):

        execute_exact_command()

    def do_fuzzy(self, arg):

        execute_fuzzy_command()

    def do_keylength(self, arg):

        execute_keylength_command()

    def do_match(self, arg):

        execute_match_command()

    def do_occurrences(self, arg):

        execute_occurrences_command()

    def do_startswith(self, arg):

        execute_startswith_command()

    def do_wordlength(self, arg):

        execute_wordlength_command()

    def do_wordmatch(self, arg):

        execute_wordmatch_command()
