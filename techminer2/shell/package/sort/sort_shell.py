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
from techminer2.shell.package.sort.commands import execute_textprocessing_command


class SortShell(BaseShell):

    prompt = make_colorized_prompt("tm2:package:sort")

    def do_textprocessing(self, arg):
        """Sort all text processing package files."""
        execute_textprocessing_command()
