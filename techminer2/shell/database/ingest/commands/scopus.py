from techminer2.ingest.data_sources import Scopus


def execute_scopus_command():

    Scopus(root_directory="./").run()
