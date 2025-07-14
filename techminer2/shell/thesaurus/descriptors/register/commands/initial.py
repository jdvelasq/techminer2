from ......thesaurus.descriptors import RegisterInitialWord
from .....colorized_input import colorized_input


def execute_initial_command():

    print()

    word = colorized_input(". new initial word > ").strip()
    if word == "":
        print()
        return

    print()
    RegisterInitialWord().having_word(word).run()
