from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.database.metrics.general.commands import execute_dataframe_command


class GeneralShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:metrics:general")

    def do_dataframe(self, arg):
        """Prints the dataset general metrics."""
        execute_dataframe_command()
