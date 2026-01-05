from techminer2.thesaurus.descriptors import CutoffFuzzyMerging


def execute_cutofffuzzy_command():

    print()
    CutoffFuzzyMerging().where_root_directory("./").run()
