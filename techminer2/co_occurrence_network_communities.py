"""
Co-occurrence Network / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> co_occurrence_network_communities(
...     'author_keywords', 
...     min_occ=4, 
...     directory=directory,
... ).head()
cluster                            CL_00  ...                    CL_03
rn                                        ...                         
0                       fintech 139:1285  ...        covid-19 008:0036
1        financial technologies 028:0225  ...            risk 007:0015
2           financial inclusion 017:0339  ...  perceived risk 006:0016
3                    regulation 011:0084  ...           trust 005:0018
4                  crowdfunding 008:0116  ...    peer-to-peer 004:0018
<BLANKLINE>
[5 rows x 4 columns]

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .network import network
from .network_communities import network_communities


def co_occurrence_network_communities(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        directory=directory,
    )

    network_ = network(
        matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_communities(network_)
