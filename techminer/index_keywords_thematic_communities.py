"""
Index keywords thematic communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> index_keywords_thematic_communities(min_occ=4, directory=directory)
cluster                         CLUST_0  ...                     CLUST_3
rn                                       ...                            
0                        fintech 48:269  ...   financial products 05:103
1                        finance 18:489  ...  financial inclusion 04:104
2                       commerce 08:369  ...            ecosystem 04:102
3          financial institution 06:150  ...                            
4                 business model 06:260  ...                            
5        artificial intelligence 06:003  ...                            
6           financial innovation 05:023  ...                            
7               electronic money 05:043  ...                            
8                    engineering 04:014  ...                            
9                     blockchain 04:222  ...                            
10            internet of things 03:023  ...                            
<BLANKLINE>
[11 rows x 4 columns]

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_communities import network_communities


def index_keywords_thematic_communities(
    min_occ=2,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="index_keywords",
        min_occ=min_occ,
        normalization="association",
        directory=directory,
    )

    network = co_occurrence_network(
        co_occurrence_matrix=coc_matrix,
        clustering_method="louvain",
        manifold_method=None,
    )

    return network_communities(network)
