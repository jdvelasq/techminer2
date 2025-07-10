from ......thesaurus.descriptors import RemoveDeterminers


def execute_determiners_command():

    print()
    RemoveDeterminers().where_root_directory_is("./").run()
