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
from techminer2.shell.system.nounphrases.nounphrases_shell import NounPhrasesShell
from techminer2.shell.system.open.open_shell import OpenShell


class SystemShell(BaseShell):

    prompt = make_colorized_prompt("tm2:system")

    def do_nounphrases(self, arg):
        """Knoun noun phrases management."""
        NounPhrasesShell().cmdloop()
        self.do_help(arg)

    def do_open(self, arg):
        """Open techminer2 system files."""
        OpenShell().cmdloop()
        self.do_help(arg)
