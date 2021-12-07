"""
Countries co-occurrence communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> countries_co_occurrence_communities(min_occ=2, directory=directory).head()
cluster             CLUST_0  ...         CLUST_9
rn                           ...                
0        south korea 11:083  ...  romania 03:007
1              india 11:026  ...                
2              spain 08:018  ...                
3             russia 08:006  ...                
4          singapore 07:252  ...                
<BLANKLINE>
[5 rows x 11 columns]


"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_communities import network_communities


def countries_co_occurrence_communities(
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="countries",
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
