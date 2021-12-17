"""
Coupling Network / Communities
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> coupling_network_communities(
...     column='author_keywords',
...     min_occ=4, 
...     top_n=20,
...     directory=directory,
... ).head()
cluster                                            CLUST_0  ...                            CLUST_3
rn                                                          ...                                   
0               Gabor D et al, 2017, NEW POLIT ECON 146:15  ...  Hu Z et al, 2019, SYMMETRY 044:14
1             Leong C et al, 2017, INT J INF MANAGE 101:16  ...                                   
2              Haddad C et al, 2019, SMALL BUS ECON 097:22  ...                                   
3                Jagtiani J et al, 2018, J ECON BUS 049:10  ...                                   
4        Kang J et al, 2018, HUM-CENTRIC COMPUT INF SCI...  ...                                   
<BLANKLINE>
[5 rows x 4 columns]


"""
import pandas as pd

from .coupling_matrix import coupling_matrix
from .network import network
from .network_communities import network_communities
from .utils import load_all_documents


def coupling_network_communities(
    column,
    top_n=100,
    min_occ=1,
    metric="global_citations",
    directory="./",
    clustering_method="louvain",
    manifold_method=None,
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

    return network_communities(network_)
