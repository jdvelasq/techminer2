"""
Thematic Map / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> thematic_map_communities(
...     'author_keywords', 
...     min_occ=4, 
...     directory=directory,
... ).head()
cluster                     CLUST_0  ...                    CLUST_4
rn                                   ...                           
0                  fintech 139:1285  ...       block-chain 017:0149
1               innovating 013:0249  ...  cryptocurrencies 008:0036
2                     bank 012:0185  ...    smart contract 004:0018
3               regulating 011:0084  ...           bitcoin 003:0007
4        financial service 011:0300  ...                           
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
