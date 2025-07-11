# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from ....base_shell import BaseShell
from .commands import (
    execute_apply_command,
    execute_cleanup_command,
    execute_initialize_command,
    execute_integrity_command,
    execute_reduce_command,
)


class GeneralShell(BaseShell):
    prompt = "tm2 > thesaurus > descriptors > general > "

    def do_apply(self, arg):
        """Apply the thesaurus to the database."""
        execute_apply_command()

    def do_cleanup(self, arg):
        """Cleanup the thesaurus."""
        execute_cleanup_command()

    def do_initialize(self, arg):
        """Create or reset the thesaurus to its initial state."""
        execute_initialize_command()

    def do_integrity(self, arg):
        """Check the integrity of the thesaurus."""
        execute_integrity_command()

    def do_reduce(self, arg):
        """Reduce the keys of the thesaurus."""
        execute_reduce_command()
