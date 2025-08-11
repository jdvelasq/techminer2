"""Commands"""
from .abbreviations import execute_abbreviations_command
from .initial import execute_initial_command
from .keyword import execute_keyword_command
from .last import execute_last_command

__all__ = [
    "execute_initial_command",
    "execute_last_command",
    "execute_keyword_command",
    "execute_abbreviations_command",
]
