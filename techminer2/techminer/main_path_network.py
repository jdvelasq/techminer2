"""
Main Path Network
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

"""
from .._lib._read_records import read_records


class _MainPathNetwork:
    def __init__(self, directory):
        self.documents = read_records(directory)
        self.run()

    def create_sequence(self):
        data = self.documents[["record_no", "local_references"]].dropna()
        data = {
            key: value.split("; ")
            for key, value in zip(data.record_no, data.local_references)
        }
        return data

    def run(self):

        sequence = self.create_sequence()

        main_path = MainPath(nodes=sequence)

        main_path.search_sources()

        main_path.build_paths()

        main_path.search_path_count()
        return
        main_path.global_key_route_search()
        self.links = main_path.links
        self.global_key_route_paths = main_path.global_key_route_paths

    def table(self):
        return

        nodes = sorted(
            set(
                [a for a, _ in self.global_key_route_paths]
                + [b for _, b in self.global_key_route_paths]
            )
        )
        documents = self.documents[["document_title", "record_no", "local_references"]]
        # documents = documents[documents.record_no.isin(nodes)]

        return documents.head()

    def main_path_network(self):
        pass


def bibliometrix__main_path_network(directory):
    return _MainPathNetwork(directory)
