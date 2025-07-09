# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....baseshell import BaseShell
from .commands import (
    execute_endswith_command,
    execute_exact_command,
    execute_fuzzy_command,
    execute_key_command,
    execute_occurrences_command,
    execute_order_command,
    execute_startswith_command,
)


class ReplaceCLI(BaseShell):
    prompt = "tm2 > thesaurus > descriptors > sort > "

    def do_endswith(self, arg):
        """Replace abbreviations."""
        execute_endswith_command()

    def do_exact(self, arg):
        """Replace abbreviations."""
        execute_exact_command()

    def do_fuzzy(self, arg):
        """Replace abbreviations."""
        execute_fuzzy_command()

    def do_key(self, arg):
        """Replace abbreviations."""
        execute_key_command()

    def do_occurrences(self, arg):
        """Replace abbreviations."""
        execute_occurrences_command()

    def do_order(self, arg):
        """Replace abbreviations."""
        execute_order_command()

    def do_startswith(self, arg):
        """Replace abbreviations."""
        execute_startswith_command()
