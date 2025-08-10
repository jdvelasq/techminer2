from techminer2.thesaurus.descriptors import SortByInitialWords


def execute_initial_command():

    print()
    SortByInitialWords().where_root_directory_is("./").run()


#
