from techminer2.thesaurus.descriptors import CombineKeys


def execute_combine_command():

    print()
    CombineKeys().where_root_directory_is("./").run()
