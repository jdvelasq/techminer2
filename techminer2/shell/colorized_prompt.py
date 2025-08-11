from colorama import Fore
from colorama import init
from colorama import Style

init(autoreset=True)


def make_colorized_prompt(prompt):

    separator = Fore.LIGHTBLACK_EX + ":" + Style.RESET_ALL

    parts = prompt.split(":")
    parts = [part.strip() for part in parts]
    parts = [
        Fore.LIGHTBLACK_EX + part + Style.RESET_ALL if i != len(parts) - 1 else part
        for i, part in enumerate(parts)
    ]

    colorized_prompt = separator.join(parts)
    colorized_prompt = colorized_prompt + Fore.LIGHTBLACK_EX + " > " + Style.RESET_ALL

    return colorized_prompt
