from techminer2.refine.thesaurus_old.descriptors import SortByWordLength


def execute_wordlength_command():

    print()
    SortByWordLength().where_root_directory("./").run()


#
