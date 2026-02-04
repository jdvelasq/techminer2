from techminer2.thesaurus_old.descriptors import RemoveStopwords


def execute_stopwords_command():

    print()
    RemoveStopwords().where_root_directory("./").run()


#
