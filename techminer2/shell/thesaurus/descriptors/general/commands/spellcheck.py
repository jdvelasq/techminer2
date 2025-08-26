from techminer2.thesaurus.descriptors import SpellCheck


def execute_spellcheck_command():

    print()
    SpellCheck().where_root_directory_is("./").run()
