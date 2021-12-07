"""
Co-occurrence communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_occurrence_communities('author_keywords', min_occ=4, directory=directory)
cluster                                   CLUST_0  ...                  CLUST_3
rn                                                 ...                         
0                                fintech 139:1285  ...        covid-19 008:0036
1                 financial technologies 028:0225  ...            risk 007:0015
2                    financial inclusion 017:0339  ...  perceived risk 006:0016
3                   peer-to-peer lending 008:0073  ...           trust 005:0018
4                   financial innovation 008:0044  ...    peer-to-peer 004:0018
5                           crowdfunding 008:0116  ...                         
6                     regulatory sandbox 006:0026  ...                         
7                    financial stability 006:0022  ...                         
8                              ecosystem 006:0016  ...                         
9                                  china 006:0018  ...                         
10                               regtech 005:0102  ...                         
11                        digitalization 005:0045  ...                         
12         sustainable development goals 004:0030  ...                         
13                        sustainability 004:0064  ...                         
14       structural equation model (sem) 004:0003  ...                         
15                               startup 004:0104  ...                         
16                            investment 004:0024  ...                         
17                    internet of things 004:0008  ...                         
18                             indonesia 004:0010  ...                         
19                       digital finance 004:0001  ...                         
<BLANKLINE>
[20 rows x 4 columns]

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_communities import network_communities


def co_occurrence_communities(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        directory=directory,
    )

    network = co_occurrence_network(
        co_occurrence_matrix=coc_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_communities(network)
