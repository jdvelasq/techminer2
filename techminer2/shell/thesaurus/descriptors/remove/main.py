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
    execute_determiners_command,
    execute_parentheses_command,
    execute_prefixes_command,
    execute_stopwords_command,
    execute_suffixes_command,
)


class RemoveCLI(BaseShell):
    prompt = "tm2 > thesaurus > descriptors > remove > "

    def do_determiners(self, arg):
        """Remove common determiners from keys."""
        execute_determiners_command()

    def do_parentheses(self, arg):
        """Remove parentheses from keys."""
        execute_parentheses_command()

    def do_prefixes(self, arg):
        """Remove common prefixes from keys."""
        execute_prefixes_command()

    def do_stopwords(self, arg):
        """Remove initial stopwords from keys."""
        execute_stopwords_command()

    def do_suffixes(self, arg):
        """Remove common suffixes from keys."""
        execute_suffixes_command()
