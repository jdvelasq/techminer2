# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ..base_shell import BaseShell
from ..colorized_prompt import make_colorized_prompt
from .ingest.ingest_shell import IngestShell
from .metrics.metrics_shell import MetricsShell
from .search.search_shell import SearchShell
from .tools.tools_shell import ToolsShell


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
