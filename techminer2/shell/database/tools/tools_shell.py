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
from techminer2.shell.database.tools.commands import execute_copyright_command
from techminer2.shell.database.tools.commands import execute_desambiguate_command
from techminer2.shell.database.tools.commands import execute_doctypes_command
from techminer2.shell.database.tools.commands import execute_generic_command
from techminer2.shell.database.tools.commands import execute_summary_command
from techminer2.shell.database.tools.commands import execute_titles_command
from techminer2.shell.database.tools.commands import execute_view_command


class ToolsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:tools")

    def do_copyright(self, arg):
        """Extract copyright text."""
        execute_copyright_command()

    def do_desambiguate(self, arg):
        """Disambiguate terms."""
        execute_desambiguate_command()

    def do_doctypes(self, arg):
        """List document types."""
        execute_doctypes_command()

    def do_generic(self, arg):
        """Determine if a term is too generic, vague or ambiguous."""
        execute_generic_command()

    def do_summary(self, arg):
        """Generate a summary."""
        execute_summary_command()

    def do_titles(self, arg):
        """Generate a Scopus search string for titles."""
        execute_titles_command()

    def do_view(self, arg):
        """View records."""
        execute_view_command()
