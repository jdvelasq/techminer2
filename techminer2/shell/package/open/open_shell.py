from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.package.open.commands import (
    execute_copyright_command,
    execute_hyphenated_command,
    execute_initial_command,
    execute_last_command,
    execute_nonhyphenated_command,
    execute_nounphrases_command,
)


class OpenShell(BaseShell):

    prompt = make_colorized_prompt("tm2:system:open")

    def do_copyright(self, arg):
        """Open copyright regex system file."""
        execute_copyright_command()

    def do_hyphenated(self, arg):
        """Open hyphenated words system file."""
        execute_hyphenated_command()

    def do_initial(self, arg):
        """Open common initial words system file."""
        execute_initial_command()

    def do_last(self, arg):
        """Open common last words system file."""
        execute_last_command()

    def do_nonhyphenated(self, arg):
        """Open non-hyphenated words system file."""
        execute_nonhyphenated_command()

    def do_nounphrases(self, arg):
        """Open known noun phrases system file."""
        execute_nounphrases_command()
