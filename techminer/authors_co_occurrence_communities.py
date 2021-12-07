"""
Authors co-occurrence communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> authors_co_occurrence_communities(min_occ=2, directory=directory).head()
cluster            CLUST_0  ...           CLUST_9
rn                          ...                  
0           Weber BW 2:228  ...  Bernards N 2:035
1           Parker C 2:228  ...                  
2        Kauffman RJ 2:228  ...                  
3           Gomber P 2:228  ...                  
<BLANKLINE>
[4 rows x 20 columns]


"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_communities import network_communities


def authors_co_occurrence_communities(
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="authors",
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
