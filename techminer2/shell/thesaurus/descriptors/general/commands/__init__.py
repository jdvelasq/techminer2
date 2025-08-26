"""Commands"""

from techminer2.shell.thesaurus.descriptors.general.commands.apply import (
    execute_apply_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.cleanup import (
    execute_cleanup_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.clump import (
    execute_clump_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.cutofffuzzy import (
    execute_cutofffuzzy_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.initialize import (
    execute_initialize_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.integrity import (
    execute_integrity_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.reduce import (
    execute_reduce_command,
)
from techminer2.shell.thesaurus.descriptors.general.commands.spellcheck import (
    execute_spellcheck_command,
)

__all__ = [
    "execute_apply_command",
    "execute_cleanup_command",
    "execute_clump_command",
    "execute_cutofffuzzy_command",
    "execute_initialize_command",
    "execute_integrity_command",
    "execute_reduce_command",
    "execute_spellcheck_command",
]
