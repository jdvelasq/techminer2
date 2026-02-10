from techminer2.refine.thesaurus_old.descriptors import CutoffFuzzyMerging


def execute_cutofffuzzy_command():

    print()
    CutoffFuzzyMerging().where_root_directory("./").run()
