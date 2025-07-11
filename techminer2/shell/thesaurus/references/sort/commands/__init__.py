"""Commands"""

from .alphabet import execute_alphabet_command
from .fuzzy import execute_fuzzy_command
from .match import execute_match_command

__all__ = [
    "execute_alphabet_command",
    "execute_fuzzy_command",
    "execute_match_command",
]
