from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import ReplaceLastWord


def execute_last_command():

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
        ReplaceLastWord()
        .where_root_directory_is("./")
        .having_word(word)
        .having_replacement(replacement)
        .run()
    )
