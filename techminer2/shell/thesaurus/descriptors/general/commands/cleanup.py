from techminer2.thesaurus.descriptors import NormalizeKeys


def execute_cleanup_command():

    print()
    NormalizeKeys().where_root_directory_is("./").run()
