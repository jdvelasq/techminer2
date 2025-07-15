# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

from ...base_shell import BaseShell
from ...colorized_prompt import make_colorized_prompt
from .commands import execute_contexts_command


class SearchShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:search")

    def do_contexts(self, arg):
        """Search text contexts."""
        execute_contexts_command()
