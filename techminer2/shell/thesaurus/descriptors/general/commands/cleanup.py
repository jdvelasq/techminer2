from techminer2.thesaurus_old.descriptors import NormalizeKeys


def execute_cleanup_command():

    print()
    NormalizeKeys().where_root_directory("./").run()
