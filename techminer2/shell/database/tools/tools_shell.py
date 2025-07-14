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
from .commands import execute_copyright_command


class ToolsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:tools")

    def do_copyright(self, arg):
        """Extract copyright text."""
        execute_copyright_command()
