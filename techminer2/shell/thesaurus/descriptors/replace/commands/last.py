from ......thesaurus.descriptors import ReplaceLastWord


def execute_last_command():

    print()
    word = input(". Enter word to replace > ").strip()
    if not word:
        print()
        return
    replacement = input(". Enter replacement word  > ").strip()
    if not replacement:
        print()
        return
    (
        ReplaceLastWord()
        .where_root_directory_is("./")
        .having_word(word)
        .having_replacement(replacement)
        .run()
    )
