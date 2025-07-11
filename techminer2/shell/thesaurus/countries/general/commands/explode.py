from ......thesaurus.countries import ExplodeKeys


def execute_explode_command():

    print()
    ExplodeKeys().where_root_directory_is("./").run()
