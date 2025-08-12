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
from techminer2.shell.system.nounphrases.commands import execute_last_command


class NounPhrasesShell(BaseShell):

    prompt = make_colorized_prompt("tm2:system:nounphrases")

    def do_last(self, arg):
        """Check variations of last word in noun phrases."""
        execute_last_command()
