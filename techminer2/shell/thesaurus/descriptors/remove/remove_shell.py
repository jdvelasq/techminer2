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
    execute_determiners_command,
    execute_initial_command,
    execute_last_command,
    execute_parentheses_command,
    execute_stopwords_command,
)


class RemoveShell(BaseShell):
    prompt = "tm2 > thesaurus > descriptors > remove > "

    def do_determiners(self, arg):
        """Remove determiners at the beginning of keys."""
        execute_determiners_command()

    def do_initial(self, arg):
        """Remove common words at the beginning of keys."""
        execute_initial_command()

    def do_last(self, arg):
        """Remove common words at the end of keys."""
        execute_last_command()

    def do_parentheses(self, arg):
        """Remove parentheses from keys."""
        execute_parentheses_command()

    def do_stopwords(self, arg):
        """Remove stopwords at the beginning of keys."""
        execute_stopwords_command()
