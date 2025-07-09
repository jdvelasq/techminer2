from ......thesaurus.descriptors import RemoveInitialDeterminers


def execute_determiners_command():

    print()
    RemoveInitialDeterminers().where_root_directory_is("./").run()
