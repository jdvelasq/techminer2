from ......thesaurus.descriptors import RemoveCommonLastWords


def execute_suffixes_command():

    print()
    RemoveCommonLastWords().where_root_directory_is("./").run()
