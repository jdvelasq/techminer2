from ......thesaurus.descriptors import ReplaceEndsWithWord


def execute_endswith_command():

    print()
    word = input(". Enter word to replace > ").strip()
    replacement = input(". Enter replacement word  > ").strip()
    ReplaceEndsWithWord().where_root_directory_is("./").having_word(
        word
    ).having_replacement(replacement).run()
