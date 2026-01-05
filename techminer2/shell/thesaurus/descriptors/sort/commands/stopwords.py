from techminer2.thesaurus.descriptors import SortByStopwords


def execute_stopwords_command():

    print()
    SortByStopwords().where_root_directory("./").run()


#
