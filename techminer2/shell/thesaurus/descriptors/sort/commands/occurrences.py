from techminer2.thesaurus.descriptors import SortByOccurrences


def execute_occurrences_command():

    print()
    SortByOccurrences().where_root_directory_is("./").run()


#
