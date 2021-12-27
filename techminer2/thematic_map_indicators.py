"""
Thematic Map / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> thematic_map_indicators(
...     'author_keywords', min_occ=4, directory=directory
... ).head()
                         num_documents  global_citations  ...  closeness  pagerank
node                                                      ...                     
adoption                             4                65  ...   0.532468  0.020583
artificial intelligence              6                30  ...   0.554054  0.023916
bank                                12               185  ...   0.594203  0.019845
bitcoin                              3                 7  ...   0.518987  0.016040
block-chain                         17               149  ...   0.621212  0.030478
<BLANKLINE>
[5 rows x 6 columns]


"""


from .co_occurrence_network_indicators import co_occurrence_network_indicators


def thematic_map_indicators(
    column,
    min_occ=2,
    directory="./",
):

    return co_occurrence_network_indicators(
        column,
        min_occ=min_occ,
        normalization="association",
        clustering_method="louvain",
        directory=directory,
    )
