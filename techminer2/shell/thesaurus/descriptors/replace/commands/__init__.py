"""Commands"""

from .abbreviations import execute_abbreviations_command
from .endswith import execute_endswith_command
from .hyphenated import execute_hyphenated_command
from .startswith import execute_startswith_command
from .word import execute_word_command

__all__ = [
    "execute_abbreviations_command",
    "execute_endswith_command",
    "execute_hyphenated_command",
    "execute_startswith_command",
    "execute_word_command",
]
