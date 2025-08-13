from techminer2.thesaurus.descriptors import ClumpKeys


def execute_clump_command():

    print()
    ClumpKeys().where_root_directory_is("./").run()
