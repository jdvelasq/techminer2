from ......thesaurus.descriptors import RegisterKeyword
from .....colorized_input import colorized_input


def execute_keyword_command():

    print()

    word = colorized_input(". new keyword > ").strip()
    if word == "":
        print()
        return

    print()
    RegisterKeyword().having_word(word).run()
