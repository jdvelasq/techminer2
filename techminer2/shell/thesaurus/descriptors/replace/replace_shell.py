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
    execute_abbreviations_command,
    execute_endswith_command,
    execute_hyphenated_command,
    execute_startswith_command,
    execute_word_command,
)


class ReplaceShell(BaseShell):

    prompt = "tm2 > thesaurus > descriptors > replace > "

    def do_abbreviations(self, arg):
        """Replace abbreviations."""
        execute_abbreviations_command()

    def do_endswith(self, arg):
        """Replace words that end with a specific string."""
        execute_endswith_command()

    def do_hyphenated(self, arg):
        """Replace hyphenated words."""
        execute_hyphenated_command()

    def do_startswith(self, arg):
        """Replace words that start with a specific string."""
        execute_startswith_command()

    def do_word(self, arg):
        """Replace specific words."""
        execute_word_command()
