from ......thesaurus.descriptors import RegisterInitialWord
from .....colorized_input import colorized_input
from ...remove.commands.initial import (
    execute_initial_command as execute_removeinitial_command,
)


def execute_initial_command():

    print()

    words = []
    while True:
        word = colorized_input(". new initial word > ").strip()
        if word == "":
            break
        words.append(word)

    print()
    for word in words:
        RegisterInitialWord().having_word(word).run()

    answer = colorized_input(". do you want to remove initial words (y/[n]) > ").strip()
    if answer.lower() == "y":
        print()
        execute_removeinitial_command()
    else:
        print()
