from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.package.open.open_shell import OpenShell
from techminer2.shell.package.sort.sort_shell import SortShell


class PackageShell(BaseShell):

    prompt = make_colorized_prompt("tm2:package")

    def do_open(self, arg):
        """Open techminer2 package files."""
        OpenShell().cmdloop()
        self.do_help(arg)

    def do_sort(self, arg):
        """Sort techminer2 package files."""
        SortShell().cmdloop()
        self.do_help(arg)
