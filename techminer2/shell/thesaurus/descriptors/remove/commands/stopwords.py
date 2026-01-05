from techminer2.thesaurus.descriptors import RemoveStopwords


def execute_stopwords_command():

    print()
    RemoveStopwords().where_root_directory("./").run()


#
