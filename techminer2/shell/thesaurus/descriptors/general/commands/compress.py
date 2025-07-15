from ......thesaurus.descriptors import CompressThesaurus


def execute_compress_command():

    print()
    CompressThesaurus().where_root_directory_is("./").run()
