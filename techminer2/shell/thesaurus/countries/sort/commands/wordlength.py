from techminer2.refine.thesaurus_old.countries import SortByWordLength


def execute_wordlength_command():

    print()
    SortByWordLength().where_root_directory("./").run()
