"""
Coupling Network / Communities
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> coupling_network_communities(
...     column='author_keywords',
...     min_occ=4, 
...     top_n=20,
...     directory=directory,
... ).head()
cluster                                              CL_00  ...                              CL_03
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
from ._read_records import read_all_records
from .network import network
from .network_communities import network_communities


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
    network_ = network(
        matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_communities(network_)
