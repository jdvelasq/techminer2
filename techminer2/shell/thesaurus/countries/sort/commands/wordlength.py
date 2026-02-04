from techminer2.thesaurus_old.countries import SortByWordLength


def execute_wordlength_command():

    print()
    SortByWordLength().where_root_directory("./").run()
