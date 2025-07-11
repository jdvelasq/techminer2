# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....base_shell import BaseShell
from .commands import execute_initialize_command


class GeneralShell(BaseShell):

    prompt = "tm2 > thesaurus > abbreviations > general > "

    def do_initialize(self, arg):
        """Create or reset the thesaurus to its initial state."""
        execute_initialize_command()
