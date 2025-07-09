from ......thesaurus.descriptors import ReplaceWord


def execute_word_command():

    print()
    word = input(". Enter word to replace > ").strip()
    replacement = input(". Enter replacement word  > ").strip()
    ReplaceWord().where_root_directory_is("./").having_word(word).having_replacement(
        replacement
    ).run()
