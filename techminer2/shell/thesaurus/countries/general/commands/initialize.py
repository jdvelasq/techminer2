from ......thesaurus.countries import InitializeThesaurus


def execute_initialize_command():

    print()
    InitializeThesaurus().where_root_directory_is("./").run()
