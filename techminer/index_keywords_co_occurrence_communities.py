"""
Index keywords co-occurrence communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> index_keywords_co_occurrence_communities(min_occ=4, directory=directory)
cluster                         CLUST_0  ...                           CLUST_2
rn                                       ...                                  
0                        fintech 48:269  ...          financial service 19:347
1                     investment 10:187  ...                      china 07:065
2          financial institution 06:150  ...  technological development 05:025
3                 business model 06:260  ...                    article 05:005
4                           bank 06:062  ...       economic development 03:150
5        artificial intelligence 06:003  ...                agriculture 03:039
6             financial products 05:103  ...                                  
7           financial innovation 05:023  ...                                  
8             financial industry 05:015  ...                                  
9               electronic money 05:043  ...                                  
10           financial inclusion 04:104  ...                                  
11                   engineering 04:014  ...                                  
12                     ecosystem 04:102  ...                                  
13               decision making 04:037  ...                                  
14                    blockchain 04:222  ...                                  
15            internet of things 03:023  ...                                  
<BLANKLINE>
[16 rows x 3 columns]

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_communities import network_communities


def index_keywords_co_occurrence_communities(
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="index_keywords",
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
