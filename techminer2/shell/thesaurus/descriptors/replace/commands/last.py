from ......thesaurus.descriptors import ReplaceLastWord


def execute_last_command():

    print()
    word = input(". Enter word to replace > ").strip()
    replacement = input(". Enter replacement word  > ").strip()
    ReplaceLastWord().where_root_directory_is("./").having_word(
        word
    ).having_replacement(replacement).run()
