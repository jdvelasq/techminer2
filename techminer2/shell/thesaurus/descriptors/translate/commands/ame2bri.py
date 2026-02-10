from techminer2.refine.thesaurus_old.descriptors import AmericanToBritishSpelling


def execute_ame2bri_command():

    print()
    AmericanToBritishSpelling().where_root_directory("./").run()


#
