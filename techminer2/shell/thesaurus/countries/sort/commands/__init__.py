"""Commands"""

from .alphabet import execute_alphabet_command
from .endswith import execute_endswith_command
from .exact import execute_exact_command
from .fuzzy import execute_fuzzy_command
from .keylength import execute_keylength_command
from .match import execute_match_command
from .startswith import execute_startswith_command
from .wordlength import execute_wordlength_command
from .wordmatch import execute_wordmatch_command

__all__ = [
    "execute_alphabet_command",
    "execute_endswith_command",
    "execute_exact_command",
    "execute_fuzzy_command",
    "execute_keylength_command",
    "execute_match_command",
    "execute_startswith_command",
    "execute_wordlength_command",
    "execute_wordmatch_command",
]
