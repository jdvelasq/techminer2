"""
Thematic Map / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> thematic_map_communities('author_keywords', min_occ=4, directory=directory)
cluster                     CLUST_0  ...                  CLUST_4
rn                                   ...                         
0                  fintech 139:1285  ...            risk 007:0015
1               innovation 013:0249  ...  perceived risk 006:0016
2                     bank 012:0185  ...           trust 005:0018
3        financial service 011:0300  ...    peer-to-peer 004:0018
4               technology 007:0192  ...                         
5                  finance 007:0052  ...                         
6           business model 006:0174  ...                         
7          venture capital 005:0055  ...                         
8                  startup 004:0104  ...                         
9              retail bank 004:0056  ...                         
10               indonesia 004:0010  ...                         
11                adoption 004:0065  ...                         
<BLANKLINE>
[12 rows x 5 columns]

"""


from .co_occurrence_communities import co_occurrence_communities


def thematic_map_communities(
    column,
    min_occ=2,
    directory="./",
):

    return co_occurrence_communities(
        column=column,
        min_occ=min_occ,
        max_occ=None,
        normalization="association",
        clustering_method="louvain",
        manifold_method=None,
        directory=directory,
    )
