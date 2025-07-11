from ......thesaurus.descriptors import SortByEndsWithMatch


def execute_endswith_command():

    print()
    SortByEndsWithMatch().where_root_directory_is("./").run()
