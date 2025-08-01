# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

from ...base_shell import BaseShell
from ...colorized_prompt import make_colorized_prompt
from .commands import (
    execute_copyright_command,
    execute_desambiguate_command,
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

    def do_desambiguate(self, arg):
        """Disambiguate terms."""
        execute_desambiguate_command()

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
