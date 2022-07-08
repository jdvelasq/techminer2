"""
Thematic Map / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> thematic_map_communities(
...     'author_keywords', 
...     min_occ=4, 
...     directory=directory,
... ).head()
cluster                         CL_00           CL_01
rn                                                   
0                       fintech 59:97  covid-19 06:08
1        financial technologies 12:32      risk 04:00
2           financial inclusion 10:14                
3                    blockchain 06:09                
4                    regulation 06:01                

"""


from .co_occurrence_network_communities import co_occurrence_network_communities


def thematic_map_communities(
    column,
    min_occ=2,
    directory="./",
):

    return co_occurrence_network_communities(
        column=column,
        min_occ=min_occ,
        max_occ=None,
        normalization="association",
        clustering_method="louvain",
        manifold_method=None,
        directory=directory,
    )
