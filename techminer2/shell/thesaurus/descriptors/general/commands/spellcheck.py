from techminer2.thesaurus_old.descriptors import SpellCheck


def execute_spellcheck_command():

    print()
    SpellCheck().where_root_directory("./").run()
