from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.descriptors.remove.commands import (
    execute_determiners_command,
    execute_initial_command,
    execute_last_command,
    execute_parentheses_command,
    execute_stopwords_command,
)


class RemoveShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:remove")

    def do_determiners(self, arg):
        """Remove initial determiners."""
        execute_determiners_command()

    def do_initial(self, arg):
        """Remove common initial words."""
        execute_initial_command()

    def do_last(self, arg):
        """Remove common trailing words."""
        execute_last_command()

    def do_parentheses(self, arg):
        """Remove expressions between parentheses."""
        execute_parentheses_command()

    def do_stopwords(self, arg):
        """Remove initial stopwords."""
        execute_stopwords_command()
