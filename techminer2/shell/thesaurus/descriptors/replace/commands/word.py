from ......thesaurus.descriptors import ReplaceWord
from .....colorized_input import colorized_input


def execute_word_command():

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
        ReplaceWord()
        .where_root_directory_is("./")
        .having_word(word)
        .having_replacement(replacement)
        .run()
    )
