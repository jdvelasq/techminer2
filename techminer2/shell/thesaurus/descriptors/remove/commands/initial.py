from ......thesaurus.descriptors import RemoveInitialWords


def execute_initial_command():

    print()
    RemoveInitialWords().where_root_directory_is("./").run()
