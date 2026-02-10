from techminer2.refine.thesaurus_old.organizations import SortByKeyLength


def execute_keylength_command():

    print()
    SortByKeyLength().where_root_directory("./").run()


#
