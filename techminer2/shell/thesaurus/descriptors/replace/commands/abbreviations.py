from techminer2.thesaurus.descriptors import ReplaceAbbreviations


def execute_abbreviations_command():

    print()
    ReplaceAbbreviations().where_root_directory_is("./").run()
