from ......thesaurus.descriptors import SortByWordMatch


def execute_wordmatch_command():

    print()
    SortByWordMatch().where_root_directory_is("./").run()
