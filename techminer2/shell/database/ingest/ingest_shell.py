from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.database.ingest.commands import execute_scopus_command


class IngestShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:ingest")

    def do_scopus(self, arg):
        """Ingest raw data from a Scopus CSV file."""
        execute_scopus_command()
