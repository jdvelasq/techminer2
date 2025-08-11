# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_reduce_command,
)
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_alphabet_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_endswith_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_exact_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_fuzzy_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_initial_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_keylength_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_last_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_match_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_occurrences_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_startswith_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_stopwords_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_wordlength_command
from techminer2.shell.thesaurus.descriptors.sort.commands import execute_wordmatch_command


class SortShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:sort")

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

    def do_initial(self, arg):
        """Sort keys by common initial words."""
        execute_initial_command()

    def do_keylength(self, arg):
        """Sort keys by key length."""
        execute_keylength_command()

    def do_last(self, arg):
        """Sort keys by common last words."""
        execute_last_command()

    def do_match(self, arg):
        """Sort keys by pattern match."""
        execute_match_command()

    def do_occurrences(self, arg):
        """Sort keys by occurrences."""
        execute_occurrences_command()

    def do_startswith(self, arg):
        """Sort keys by starting pattern."""
        execute_startswith_command()

    def do_stopwords(self, arg):
        """Sort keys by stopwords."""
        execute_stopwords_command()

    def do_wordlength(self, arg):
        """Sort keys by word length."""
        execute_wordlength_command()

    def do_wordmatch(self, arg):
        """Sort keys by word match."""
        execute_wordmatch_command()

    def do_reduce(self, arg):
        """Reduce thesaurus keys."""
        execute_reduce_command()
