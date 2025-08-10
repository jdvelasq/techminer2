from techminer2.thesaurus.references import IntegrityCheck


def execute_integrity_command():

    print()
    IntegrityCheck().where_root_directory_is("./").run()


#
