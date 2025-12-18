"""Simple UI message functions."""

import sys

from colorama import Fore, Style, init

init()


def internal__ui_msg(
    msg: str,
    level: str = "INFO",
    level_color: str = Fore.LIGHTBLACK_EX,
    msg_color: str = Fore.WHITE,
    end: str = "\n",
):
    sys.stderr.write(
        f"{level_color}{level}:{Style.RESET_ALL} {msg_color}{msg}{Style.RESET_ALL}{end}"
    )
    sys.stderr.flush()
