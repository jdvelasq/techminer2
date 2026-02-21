from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.system.descriptors.descriptors_shell import (
    DescriptorsShell,
)


class SystemShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:system")

    def do_descriptors(self, arg):
        """Manage system thesaurus operations for global descriptors."""
        DescriptorsShell().cmdloop()
        self.do_help(arg)
