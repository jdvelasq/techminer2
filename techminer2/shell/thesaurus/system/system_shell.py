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
from .descriptors.descriptors_shell import DescriptorsShell


class SystemShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:system")

    def do_descriptors(self, arg):
        """Manage system thesaurus operations for global descriptors."""
        DescriptorsShell().cmdloop()
        self.do_help(arg)
