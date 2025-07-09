from ......thesaurus.descriptors import CleanupThesaurus


def execute_cleanup_command():

    print()
    CleanupThesaurus().where_root_directory_is("./").run()
