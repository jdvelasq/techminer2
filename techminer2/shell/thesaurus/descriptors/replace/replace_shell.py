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
    execute_hyphenated_command,
    execute_initial_command,
    execute_last_command,
    execute_word_command,
)


class ReplaceShell(BaseShell):

    prompt = "tm2 > thesaurus > descriptors > replace > "

    def do_abbreviations(self, arg):
        """Replace abbreviations."""
        execute_abbreviations_command()

    def do_last(self, arg):
        """Replace common last words."""
        execute_last_command()

    def do_hyphenated(self, arg):
        """Replace hyphenated words."""
        execute_hyphenated_command()

    def do_initial(self, arg):
        """Replace common initial words."""
        execute_initial_command()

    def do_word(self, arg):
        """Replace a specific word."""
        execute_word_command()
