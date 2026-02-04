from techminer2.thesaurus_old.countries import ExplodeKeys


def execute_explode_command():

    print()
    ExplodeKeys().where_root_directory("./").run()
