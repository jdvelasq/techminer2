from techminer2.refine.thesaurus_old.descriptors import RemoveDeterminers


def execute_determiners_command():

    print()
    RemoveDeterminers().where_root_directory("./").run()


#
