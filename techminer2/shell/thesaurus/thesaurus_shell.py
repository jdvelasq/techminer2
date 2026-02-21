"""Command line interface for the Thesaurus subsystem."""

from techminer2.shell.base_shell import BaseShell
from techminer2.shell.colorized_prompt import make_colorized_prompt
from techminer2.shell.thesaurus.acronyms.acronyms_shell import AcronymsShell
from techminer2.shell.thesaurus.countries.countries_shell import CountriesShell
from techminer2.shell.thesaurus.descriptors.descriptors_shell import DescriptorsShell
from techminer2.shell.thesaurus.organizations.organizations_shell import (
    OrganizationsShell,
)
from techminer2.shell.thesaurus.references.references_shell import ReferencesShell
from techminer2.shell.thesaurus.system.system_shell import SystemShell


class ThesaurusShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus")

    def do_acronyms(self, arg):
        """Manage thesaurus for acronyms."""
        AcronymsShell().cmdloop()
        self.do_help(arg)

    def do_countries(self, arg):
        """Manage thesaurus for countries."""
        CountriesShell().cmdloop()
        self.do_help(arg)

    def do_descriptors(self, arg):
        """Manage thesaurus for record descriptors."""
        DescriptorsShell().cmdloop()
        self.do_help(arg)

    def do_organizations(self, arg):
        """Manage thesaurus for organizations."""
        OrganizationsShell().cmdloop()
        self.do_help(arg)

    def do_references(self, arg):
        """Manage thesaurus for references."""
        ReferencesShell().cmdloop()
        self.do_help(arg)

    def do_system(self, arg):
        """Manage system thesaurus."""
        SystemShell().cmdloop()
        self.do_help(arg)
        self.do_help(arg)
