"""
Coupling network
===============================================================================

Builds a coupling network from a coupling matrix.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> matrix = coupling_by_column_matrix(
...     column='author_keywords',
...     min_occ=4, 
...     top_n=20,
...     directory=directory,
... )
>>> coupling_network(matrix, directory=directory).keys()
dict_keys(['nodes', 'edges', 'G', 'indicators', 'communities', 'manifold_data'])


"""
import pandas as pd

from .network import network
from .utils import load_all_documents


def coupling_network(
    coupling_matrix,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):
    # -------------------------------------------------------------------------
    # Rename axis of the matrix

    coupling_matrix = coupling_matrix.copy()
    documents = load_all_documents(directory)
    records2ids = dict(zip(documents.record_no, documents.document_id))
    records2global_citations = dict(
        zip(documents.record_no, documents.global_citations)
    )
    records2local_citations = dict(zip(documents.record_no, documents.local_citations))

    new_indexes = coupling_matrix.columns.copy()
    new_indexes = [
        (
            records2ids[index],
            records2global_citations[index],
            records2local_citations[index],
        )
        for index in new_indexes
    ]
    new_indexes = pd.MultiIndex.from_tuples(
        new_indexes, names=["document", "global_citations", "local_citations"]
    )

    coupling_matrix.columns = new_indexes.copy()
    coupling_matrix.index = new_indexes.copy()

    return co_occurrence_network(
        coupling_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )
