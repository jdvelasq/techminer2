from ......thesaurus.descriptors import RemoveInitialWords


def execute_prefixes_command():

    print()
    RemoveInitialWords().where_root_directory_is("./").run()
