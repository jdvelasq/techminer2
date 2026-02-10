from techminer2.refine.thesaurus_old.descriptors import ClumpKeys


def execute_clump_command():

    print()
    ClumpKeys().where_root_directory("./").run()
