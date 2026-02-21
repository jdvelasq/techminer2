from .copyright import execute_copyright_command
from .hyphenated import execute_hyphenated_command
from .initial import execute_initial_command
from .last import execute_last_command
from .nonhyphenated import execute_nonhyphenated_command
from .nounphrases import execute_nounphrases_command

__all__ = [
    "execute_copyright_command",
    "execute_nounphrases_command",
    "execute_initial_command",
    "execute_last_command",
    "execute_hyphenated_command",
    "execute_nonhyphenated_command",
]
