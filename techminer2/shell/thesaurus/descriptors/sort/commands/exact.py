from ......thesaurus.descriptors import SortByExactMatch


def execute_exact_command():

    print()
    SortByExactMatch().where_root_directory_is("./").run()
