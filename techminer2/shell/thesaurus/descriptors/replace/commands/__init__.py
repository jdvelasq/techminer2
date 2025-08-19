"""Commands"""

from .abbreviations import execute_acronyms_command
from .hyphenated import execute_hyphenated_command
from .initial import execute_initial_command
from .last import execute_last_command
from .word import execute_word_command

__all__ = [
    "execute_acronyms_command",
    "execute_last_command",
    "execute_hyphenated_command",
    "execute_initial_command",
    "execute_word_command",
]
