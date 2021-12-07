"""
Institutions co-occurrence communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> institutions_co_occurrence_communities(min_occ=2, directory=directory).head()
cluster                                  CLUST_0  ...                                            CLUST_9
rn                                                ...                                                   
0                 University of Latvia LVA 4:042  ...                    Universidad de Oviedo ESP 2:012
1                   Kingdom University BHR 3:039  ...  Financial University Under The Government of T...
2                  University of Malta MLT 2:029  ...                                                   
3        University College of Bahrain BHR 2:037  ...                                                   
4                University of Bahrain BHR 1:002  ...                                                   
<BLANKLINE>
[5 rows x 50 columns]


"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_communities import network_communities


def institutions_co_occurrence_communities(
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="institutions",
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
