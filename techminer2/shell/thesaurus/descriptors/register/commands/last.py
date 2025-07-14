from ......thesaurus.descriptors import RegisterLastWord
from .....colorized_input import colorized_input


def execute_last_command():

    print()

    word = colorized_input(". new last word > ").strip()
    if word == "":
        print()
        return

    print()
    RegisterLastWord().having_word(word).run()
