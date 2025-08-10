# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....base_shell import BaseShell
from ....colorized_prompt import make_colorized_prompt
from .commands import (execute_abbreviations_command, execute_initial_command,
                       execute_keyword_command, execute_last_command)


class RegisterShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:register")

    def do_abbreviations(self, arg):
        """Register abbreviations as system known phrases."""
        execute_abbreviations_command()

    def do_initial(self, arg):
        """Register new initial word."""
        execute_initial_command()

    def do_last(self, arg):
        """Register new last word."""
        execute_last_command()

    def do_keyword(self, arg):
        """Register new keyword."""
        execute_keyword_command()
