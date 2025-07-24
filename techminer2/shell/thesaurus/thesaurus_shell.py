# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""Command line interface for the Thesaurus subsystem."""


from ..base_shell import BaseShell
from ..colorized_prompt import make_colorized_prompt
from .abbreviations.abbreviations_shell import AbbreviationsShell
from .countries.countries_shell import CountriesShell
from .descriptors.descriptors_shell import DescriptorsShell
from .organizations.organizations_shell import OrganizationsShell
from .references.references_shell import ReferencesShell
from .system.system_shell import SystemShell


class ThesaurusShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus")

    def do_abbreviations(self, arg):
        """Manage thesaurus for abbreviations."""
        AbbreviationsShell().cmdloop()
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
