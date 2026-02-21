from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.database.ingest.ingest_shell import IngestShell
from techminer2.shell.database.metrics.metrics_shell import MetricsShell
from techminer2.shell.database.search.search_shell import SearchShell
from techminer2.shell.database.tools.tools_shell import ToolsShell


class DatabaseShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database")

    def do_ingest(self, arg):
        """Ingest raw data into the database."""
        IngestShell().cmdloop()
        self.do_help(arg)

    def do_metrics(self, arg):
        """Analyze and compute dataset metrics."""
        MetricsShell().cmdloop()
        self.do_help(arg)

    def do_search(self, arg):
        """Access the search tools."""
        SearchShell().cmdloop()
        self.do_help(arg)

    def do_tools(self, arg):
        """Access the tools for data processing."""
        ToolsShell().cmdloop()
        self.do_help(arg)
