from .....database.ingest import IngestScopus


def execute_scopus_command():

    IngestScopus(root_directory="./").run()
