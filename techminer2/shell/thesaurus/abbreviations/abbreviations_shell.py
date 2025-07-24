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
from .general.general_shell import GeneralShell
from .register.register_shell import RegisterShell


class AbbreviationsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:abbreviations")

    def do_general(self, arg):
        """General commands."""
        GeneralShell().cmdloop()
        self.do_help(arg)

    def do_register(self, arg):
        """Register new noun phrases in the system."""
        RegisterShell().cmdloop()
        self.do_help(arg)
