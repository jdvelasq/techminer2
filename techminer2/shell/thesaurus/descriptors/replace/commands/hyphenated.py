from ......thesaurus.descriptors import ReplaceHyphenatedWords


def execute_hyphenated_command():

    print()
    ReplaceHyphenatedWords().where_root_directory_is("./").run()
