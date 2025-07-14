from ......thesaurus.descriptors import ReplaceInitialWord
from .....colorized_input import colorized_input


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
        .where_root_directory_is("./")
        .having_word(word)
        .having_replacement(replacement)
        .run()
    )
