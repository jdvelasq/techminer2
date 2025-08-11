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
from techminer2.shell.thesaurus.system.descriptors.sort.sort_shell import SortShell


class DescriptorsShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:system:descriptors")

    def do_sort(self, arg):
        """Sort the thesaurus."""
        SortShell().cmdloop()
        self.do_help(arg)
