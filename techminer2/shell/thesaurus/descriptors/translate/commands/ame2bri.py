from ......thesaurus.descriptors import AmericanToBritishSpelling


def execute_ame2bri_command():

    print()
    AmericanToBritishSpelling().where_root_directory_is("./").run()
