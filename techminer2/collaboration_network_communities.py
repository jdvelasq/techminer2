"""
Collaboration Network / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> collaboration_network_communities('authors', min_occ=2, directory=directory).head()
cluster              CL_00  ...           CL_19
rn                          ...                
0           Weber BW 2:228  ...  Wojcik D 5:019
1           Parker C 2:228  ...                
2        Kauffman RJ 2:228  ...                
3           Gomber P 2:228  ...                
<BLANKLINE>
[4 rows x 20 columns]

"""
from .co_occurrence_network_communities import co_occurrence_network_communities


def collaboration_network_communities(
    column,
    min_occ=2,
    normalization="association",
    clustering_method="louvain",
    directory="./",
):

    if column not in ["authors", "institutions", "countries"]:
        raise ValueError("The column must be 'authors', 'institutions' or 'countries'")

    return co_occurrence_network_communities(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        directory=directory,
    )
