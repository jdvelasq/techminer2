from techminer2.thesaurus_old.descriptors import ReplaceHyphenatedWords


def execute_hyphenated_command():

    print()
    ReplaceHyphenatedWords().where_root_directory("./").run()
