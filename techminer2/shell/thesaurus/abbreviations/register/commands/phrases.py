from ......thesaurus.abbreviations import RegisterPhrases


def execute_phrases_command():

    RegisterPhrases().where_root_directory_is("./").run()
