from ......thesaurus.descriptors import SortByLastWords


def execute_last_command():

    print()
    SortByLastWords().where_root_directory_is("./").run()
