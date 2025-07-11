# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....base_shell import BaseShell
from .commands.ame2bri import execute_ame2bri_command
from .commands.bri2ame import execute_bri2ame_command


class TranslateShell(BaseShell):

    prompt = "tm2 > thesaurus > descriptors > translate > "

    def do_ame2bri(self, arg):
        """Translate American English to British English."""
        execute_ame2bri_command()

    def do_bri2ame(self, arg):
        """Translate British English to American English."""
        execute_bri2ame_command()

    def do_back(self, arg):
        """Go back to the previous menu."""
        return True
