"""Commands"""

from techminer2.shell.thesaurus.descriptors.clean.commands.combine import (
    execute_combine_command,
)
from techminer2.shell.thesaurus.descriptors.clean.commands.desambiguate import (
    execute_desambiguate_command,
)
from techminer2.shell.thesaurus.descriptors.clean.commands.generic import (
    execute_generic_command,
)

__all__ = [
    "execute_combine_command",
    "execute_desambiguate_command",
    "execute_generic_command",
]
