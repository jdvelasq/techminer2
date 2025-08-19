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
from techminer2.shell.thesaurus.descriptors.replace.commands import (
    execute_acronyms_command,
)
from techminer2.shell.thesaurus.descriptors.replace.commands import (
    execute_hyphenated_command,
)
from techminer2.shell.thesaurus.descriptors.replace.commands import (
    execute_initial_command,
)
from techminer2.shell.thesaurus.descriptors.replace.commands import execute_last_command
from techminer2.shell.thesaurus.descriptors.replace.commands import execute_word_command


class ReplaceShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:replace")

    def do_acronyms(self, arg):
        """Replace acronyms."""
        execute_acronyms_command()

    def do_hyphenated(self, arg):
        """Replace hyphenated words."""
        execute_hyphenated_command()

    def do_initial(self, arg):
        """Replace common initial words."""
        execute_initial_command()

    def do_last(self, arg):
        """Replace common last words."""
        execute_last_command()

    def do_word(self, arg):
        """Replace a specific word."""
        execute_word_command()
