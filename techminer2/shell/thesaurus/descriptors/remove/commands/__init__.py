"""Commands."""
from .determiners import execute_determiners_command
from .initial import execute_initial_command
from .last import execute_last_command
from .parentheses import execute_parentheses_command
from .stopwords import execute_stopwords_command

__all__ = [
    "execute_determiners_command",
    "execute_initial_command",
    "execute_last_command",
    "execute_parentheses_command",
    "execute_stopwords_command",
]
