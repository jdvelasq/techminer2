from ......thesaurus.descriptors import RemoveInitialStopwords


def execute_stopwords_command():

    print()
    RemoveInitialStopwords().where_root_directory_is("./").run()
