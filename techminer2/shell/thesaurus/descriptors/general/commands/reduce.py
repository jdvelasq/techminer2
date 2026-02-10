from techminer2.refine.thesaurus_old.descriptors import ReduceKeys


def execute_reduce_command():

    print()
    ReduceKeys().where_root_directory("./").run()
