from techminer2.thesaurus.countries import ReduceKeys


def execute_reduce_command():

    print()
    ReduceKeys().where_root_directory_is("./").run()
