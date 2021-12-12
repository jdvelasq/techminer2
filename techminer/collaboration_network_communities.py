"""
Collaboration Network / Communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> collaboration_network_communities('authors', min_occ=2, directory=directory).head()
cluster            CLUST_0  ...           CLUST_9
rn                          ...                  
0           Weber BW 2:228  ...  Bernards N 2:035
1           Parker C 2:228  ...                  
2        Kauffman RJ 2:228  ...                  
3           Gomber P 2:228  ...                  
<BLANKLINE>
[4 rows x 20 columns]

"""
from .co_occurrence_communities import co_occurrence_communities


def collaboration_network_communities(
    column,
    min_occ=2,
    normalization="association",
    clustering_method="louvain",
    directory="./",
):

    if column not in ["authors", "institutions", "countries"]:
        raise ValueError("The column must be 'authors', 'institutions' or 'countries'")

    return co_occurrence_communities(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        directory=directory,
    )
