"""Commands"""

from techminer2.shell.thesaurus.descriptors.clean.commands.combine import (
    execute_combine_command,
)
from techminer2.shell.thesaurus.descriptors.clean.commands.stopwords import (
    execute_stopwords_command,
)
from techminer2.shell.thesaurus.descriptors.clean.commands.synonyms import (
    execute_synonyms_command,
)

__all__ = [
    "execute_combine_command",
    "execute_synonyms_command",
    "execute_stopwords_command",
]
