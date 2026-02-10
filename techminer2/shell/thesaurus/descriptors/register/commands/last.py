from techminer2.refine.thesaurus_old.descriptors import RegisterLastWord
from techminer2.shell.colorized_input import colorized_input
from techminer2.shell.thesaurus.descriptors.remove.commands.last import (
    execute_last_command as execute_removelast_command,
)


def execute_last_command():

    print()

    words = []
    while True:
        word = colorized_input(". new last word > ").strip()
        if word == "":
            break
        words.append(word.upper().strip())

    print()
    RegisterLastWord().having_word(words).run()

    answer = colorized_input(". do you want to remove last words (y/[n]) > ").strip()
    if answer.lower() == "y":
        print()
        execute_removelast_command()
    else:
        print()


#
