from techminer2.thesaurus_old.descriptors import ReplaceAcronyms


def execute_acronyms_command():

    print()
    ReplaceAcronyms().where_root_directory("./").run()
