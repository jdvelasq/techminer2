from ......thesaurus.abbreviations import CreateThesaurus


def execute_create_command():

    print()
    CreateThesaurus().where_root_directory_is("./").run()
