from techminer2.thesaurus_old.countries import SortByKeyLength


def execute_keylength_command():

    print()
    SortByKeyLength().where_root_directory("./").run()
