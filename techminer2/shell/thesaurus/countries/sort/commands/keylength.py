from techminer2.thesaurus.countries import SortByKeyLength


def execute_keylength_command():

    print()
    SortByKeyLength().where_root_directory("./").run()
