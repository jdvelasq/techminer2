from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus_old.descriptors import ReplaceInitialWord


def execute_initial_command():

    print()

    word = colorized_input(". Enter word to replace > ").strip()
    if not word:
        print()
        return

    replacement = colorized_input(". Enter replacement word  > ").strip()
    if not replacement:
        print()
        return

    print()
    (
        ReplaceInitialWord()
        .where_root_directory("./")
        .having_word(word)
        .having_replacement(replacement)
        .run()
    )
