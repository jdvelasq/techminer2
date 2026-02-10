from techminer2.refine.thesaurus_old.countries import ExplodeKeys


def execute_explode_command():

    print()
    ExplodeKeys().where_root_directory("./").run()
