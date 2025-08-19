from techminer2.thesaurus.acronyms import RegisterPhrases


def execute_phrases_command():
    print()
    RegisterPhrases().where_root_directory_is("./").run()
