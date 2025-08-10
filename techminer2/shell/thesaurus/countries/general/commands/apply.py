from techminer2.thesaurus.countries import ApplyThesaurus


def execute_apply_command():

    print()
    ApplyThesaurus().where_root_directory_is("./").run()
