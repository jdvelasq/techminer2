from techminer2.refine.thesaurus_old.descriptors import BritishToAmericanSpelling


def execute_bri2ame_command():

    print()
    BritishToAmericanSpelling().where_root_directory("./").run()


#
