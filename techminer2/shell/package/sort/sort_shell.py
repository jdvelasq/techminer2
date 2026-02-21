from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.package.sort.commands import execute_textprocessing_command


class SortShell(BaseShell):

    prompt = make_colorized_prompt("tm2:package:sort")

    def do_textprocessing(self, arg):
        """Sort all text processing package files."""
        execute_textprocessing_command()
