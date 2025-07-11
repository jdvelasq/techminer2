from ......thesaurus.descriptors import ReplaceInitialWord


def execute_initial_command():

    print()
    word = input(". Enter word to replace > ").strip()
    replacement = input(". Enter replacement word  > ").strip()
    ReplaceInitialWord().where_root_directory_is("./").having_word(
        word
    ).having_replacement(replacement).run()
