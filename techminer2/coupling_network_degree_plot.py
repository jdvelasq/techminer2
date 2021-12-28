"""
Coupling Network / Degree Plot
===============================================================================

Builds a coupling network from a coupling matrix.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/coupling_network_degree_plot.png"
>>> coupling_network_degree_plot(
...     column='author_keywords',
...     min_occ=4, 
...     top_n=20,
...     directory=directory,
... ).savefig(file_name)

.. image:: images/coupling_network_degree_plot.png
    :width: 700px
    :align: center

"""
import pandas as pd

from .coupling_matrix import coupling_matrix
from .load_all_documents import load_all_documents
from .records2documents import records2documents
from .network import network
from .network_degree_plot import network_degree_plot


def coupling_network_degree_plot(
    column,
    top_n=100,
    min_occ=1,
    metric="global_citations",
    directory="./",
    clustering_method="louvain",
    manifold_method=None,
    figsize=(7, 7),
):
    # -------------------------------------------------------------------------
    # Documents
    matrix = coupling_matrix(
        column=column,
        top_n=top_n,
        min_occ=min_occ,
        metric=metric,
        directory=directory,
    )

    # -------------------------------------------------------------------------
    # Rename axis of the matrix
    # documents = load_all_documents(directory)
    # records2ids = dict(zip(documents.record_no, documents.document_id))
    # records2global_citations = dict(
    #     zip(documents.record_no, documents.global_citations)
    # )
    # records2local_citations = dict(zip(documents.record_no, documents.local_citations))

    # new_indexes = matrix.columns.get_level_values(0)
    # new_indexes = [
    #     (
    #         records2ids[index],
    #         records2global_citations[index],
    #         records2local_citations[index],
    #     )
    #     for index in new_indexes
    # ]
    # new_indexes = pd.MultiIndex.from_tuples(
    #     new_indexes, names=["document", "global_citations", "local_citations"]
    # )

    # matrix.columns = new_indexes.copy()
    # matrix.index = new_indexes.copy()

    network_ = network(
        matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_degree_plot(
        network_,
        figsize=figsize,
    )
