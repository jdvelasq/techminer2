from techminer2.refine.thesaurus_old.countries import ApplyThesaurus


def execute_apply_command():

    print()
    ApplyThesaurus().where_root_directory("./").run()
