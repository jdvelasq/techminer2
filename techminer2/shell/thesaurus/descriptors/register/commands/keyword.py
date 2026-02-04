from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus_old.descriptors import RegisterKeyword


def execute_keyword_command():

    print()
    words = []
    while True:
        word = colorized_input(". new keyword > ").strip()
        if word.strip() == "":
            break
        words.append(word.upper().strip())

    if not words:
        print()
        return

    print()
    RegisterKeyword().having_word(words).run()
