from ......thesaurus.descriptors import SortByStopwords


def execute_stopwords_command():

    print()
    SortByStopwords().where_root_directory_is("./").run()
