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
from techminer2.shell.package.open.commands import execute_copyright_command
from techminer2.shell.package.open.commands import execute_nounphrases_command


class OpenShell(BaseShell):

    prompt = make_colorized_prompt("tm2:system:open")

    def do_copyright(self, arg):
        """Open copyright regex system file."""
        execute_copyright_command()

    def do_nounphrases(self, arg):
        """Open known noun phrases system file."""
        execute_nounphrases_command()
