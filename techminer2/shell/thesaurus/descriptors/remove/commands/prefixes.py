from ......thesaurus.descriptors import RemovePrefixes


def execute_prefixes_command():

    print()
    RemovePrefixes().where_root_directory_is("./").run()
