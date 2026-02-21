from colorama import Fore, init

init(autoreset=True)


def colorized_input(prompt):

    prompt = prompt.replace(".", Fore.LIGHTBLACK_EX + "." + Fore.RESET)
    prompt = prompt.replace(">", Fore.LIGHTBLACK_EX + ">" + Fore.RESET)

    return input(prompt).strip()
