from ......thesaurus.descriptors import SortByFuzzyMatch


def execute_fuzzy_command():

    print()
    SortByFuzzyMatch().where_root_directory_is("./").run()
