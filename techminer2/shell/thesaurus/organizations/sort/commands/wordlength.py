from techminer2.refine.thesaurus_old.organizations import SortByWordLength


def execute_wordlength_command():

    print()
    SortByWordLength().where_root_directory("./").run()


#
