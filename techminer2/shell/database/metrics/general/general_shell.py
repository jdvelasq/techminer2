# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

from ....base_shell import BaseShell
from .commands import execute_dataframe_command


class GeneralShell(BaseShell):

    prompt = "tm2 > database > metrics > general > "

    def do_dataframe(self, arg):
        """Prints the dataset general metrics."""
        execute_dataframe_command()
