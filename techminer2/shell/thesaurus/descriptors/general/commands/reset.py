from ......thesaurus.descriptors import CreateThesaurus


def execute_reset_command():

    print()
    CreateThesaurus().where_root_directory_is("./").run()
