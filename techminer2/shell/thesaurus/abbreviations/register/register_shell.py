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
from techminer2.shell.thesaurus.abbreviations.register.commands import (
    execute_phrases_command,
)


class RegisterShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:abbreviations:register")

    def do_phrases(self, arg):
        """Register new noun phrases in the system."""
        execute_phrases_command()
