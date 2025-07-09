from ......thesaurus.descriptors import SortByEndsWithKeyMatch


def execute_endswith_command():

    print()
    SortByEndsWithKeyMatch().where_root_directory_is("./").run()
