from ......thesaurus.descriptors import SortByStartsWithMatch


def execute_startswith_command():

    print()
    SortByStartsWithMatch().where_root_directory_is("./").run()
