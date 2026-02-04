from techminer2.thesaurus_old.countries import IntegrityCheck


def execute_integrity_command():

    print()
    IntegrityCheck().where_root_directory("./").run()
