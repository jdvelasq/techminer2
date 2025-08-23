# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.descriptors.clean.commands import (
    execute_combine_command,
    execute_stopwords_command,
    execute_synonyms_command,
)


class CleanShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:clean")

    def do_combine(self, arg):
        """Combine thesaurus keys."""
        execute_combine_command()

    def do_synonyms(self, arg):
        """Determine if two terms are conceptual synonyms."""
        execute_synonyms_command()

    def do_stopwords(self, arg):
        """Determine if a term is too generic, vague or ambiguous."""
        execute_stopwords_command()
