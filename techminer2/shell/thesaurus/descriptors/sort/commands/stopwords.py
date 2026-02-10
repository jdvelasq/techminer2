from techminer2.refine.thesaurus_old.descriptors import SortByStopwords


def execute_stopwords_command():

    print()
    SortByStopwords().where_root_directory("./").run()


#
