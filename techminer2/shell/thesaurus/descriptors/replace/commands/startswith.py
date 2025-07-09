from ......thesaurus.descriptors import ReplaceStartsWithWord


def execute_startswith_command():

    print()
    word = input(". Enter word to replace > ").strip()
    replacement = input(". Enter replacement word  > ").strip()
    ReplaceStartsWithWord().where_root_directory_is("./").having_word(
        word
    ).having_replacement(replacement).run()
