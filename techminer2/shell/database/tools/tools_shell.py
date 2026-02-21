from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.database.tools.commands import (
    execute_colons_command,
    execute_copyright_command,
    execute_doctypes_command,
    execute_summary_command,
    execute_titles_command,
    execute_view_command,
)


class ToolsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:database:tools")

    def do_copyright(self, arg):
        """Extract copyright text."""
        execute_copyright_command()

    def do_colons(self, arg):
        """Extract colons text."""
        execute_colons_command()

    def do_doctypes(self, arg):
        """List document types."""
        execute_doctypes_command()

    def do_summary(self, arg):
        """Generate a summary."""
        execute_summary_command()

    def do_titles(self, arg):
        """Generate a Scopus search string for titles."""
        execute_titles_command()

    def do_view(self, arg):
        """View records."""
        execute_view_command()


#
