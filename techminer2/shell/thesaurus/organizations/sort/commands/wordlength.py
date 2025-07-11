from ......thesaurus.organizations import SortByWordLength


def execute_wordlength_command():

    print()
    SortByWordLength().where_root_directory_is("./").run()
