"""Command line interface for the Thesaurus subsystem."""

from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.zotero.commands import (
    execute_search_command,
    execute_update_command,
)


class ZoteroShell(BaseShell):

    prompt = make_colorized_prompt("tm2:zotero")

    def do_update(self, arg):
        """Update Zotero database."""
        execute_update_command()

    def do_search(self, arg):
        """Search database by UTs."""
        execute_search_command()
