from ......thesaurus.descriptors import BritishToAmericanSpelling


def execute_bri2ame_command():

    print()
    BritishToAmericanSpelling().where_root_directory_is("./").run()
