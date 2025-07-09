"""Commands."""

from .determiners import execute_determiners_command
from .parentheses import execute_parentheses_command
from .prefixes import execute_prefixes_command
from .stopwords import execute_stopwords_command
from .suffixes import execute_suffixes_command

__all__ = [
    "execute_determiners_command",
    "execute_parentheses_command",
    "execute_prefixes_command",
    "execute_stopwords_command",
    "execute_suffixes_command",
]
