from techminer2.thesaurus.descriptors import ReplaceAcronyms


def execute_acronyms_command():

    print()
    ReplaceAcronyms().where_root_directory_is("./").run()
