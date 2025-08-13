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
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_apply_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_cleanup_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_clump_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_initialize_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_integrity_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands import (
    execute_reduce_command,
)


class GeneralShell(BaseShell):

    prompt = make_colorized_prompt("tm2:thesaurus:descriptors:general")

    def do_apply(self, arg):
        """Apply the thesaurus."""
        execute_apply_command()

    def do_cleanup(self, arg):
        """Clean up the thesaurus."""
        execute_cleanup_command()

    def do_clump(self, arg):
        """Clump thesaurus keys."""
        execute_clump_command()

    def do_initialize(self, arg):
        """Reset or create the thesaurus."""
        execute_initialize_command()

    def do_integrity(self, arg):
        """Verify thesaurus integrity."""
        execute_integrity_command()

    def do_reduce(self, arg):
        """Reduce thesaurus keys."""
        execute_reduce_command()
