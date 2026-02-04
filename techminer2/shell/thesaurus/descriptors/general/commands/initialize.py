from techminer2.thesaurus_old.descriptors import InitializeThesaurus


def execute_initialize_command():

    print()
    InitializeThesaurus().where_root_directory("./").run()
