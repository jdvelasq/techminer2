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
    execute_desambiguate_command,
    execute_generic_command,
)


class CleanShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:clean")

    def do_combine(self, arg):
        """Combine thesaurus keys."""
        execute_combine_command()

    def do_desambiguate(self, arg):
        """Disambiguate terms."""
        execute_desambiguate_command()

    def do_generic(self, arg):
        """Determine if a term is too generic, vague or ambiguous."""
        execute_generic_command()
