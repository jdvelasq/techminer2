from ......thesaurus.descriptors import SortByMatch


def execute_match_command():

    print()
    SortByMatch().where_root_directory_is("./").run()
