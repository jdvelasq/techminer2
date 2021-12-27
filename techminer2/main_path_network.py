"""
Main Path Network
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"

"""
from .documents_api.load_filtered_documents import load_filtered_documents


class _MainPathNetwork:
    def __init__(self, directory):
        self.documents = load_filtered_documents(directory)
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


def main_path_network(directory):
    return _MainPathNetwork(directory)
