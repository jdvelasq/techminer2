"""
Thematic Map / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> thematic_map_communities(
...     'author_keywords', 
...     min_occ=4, 
...     directory=directory,
... ).head()
cluster                       CL_00  ...                         CL_04
rn                                   ...                              
0               innovation 013:0249  ...  financial inclusion 017:0339
1                     bank 012:0185  ...              regtech 005:0102
2        financial service 011:0300  ...       digitalization 005:0045
3               regulation 011:0084  ...  fintech-innovations 005:0002
4               technology 007:0192  ...       sustainability 004:0064
<BLANKLINE>
[5 rows x 5 columns]

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
