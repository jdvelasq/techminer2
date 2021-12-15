"""
Thematic Map / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> thematic_map_indicators(
...     'author_keywords', min_occ=4, directory=directory
... ).head()
                         num_documents  global_citations  ...  closeness  pagerank
node                                                      ...                     
adoption                             4                65  ...   0.532468  0.021204
artificial intelligence              6                30  ...   0.554054  0.024433
bank                                12               185  ...   0.585714  0.019673
bitcoin                              3                 7  ...   0.518987  0.016266
blockchain                          17               149  ...   0.621212  0.031094
<BLANKLINE>
[5 rows x 6 columns]


"""


from .co_occurrence_indicators import co_occurrence_indicators


def thematic_map_indicators(
    column,
    min_occ=2,
    directory="./",
):

    return co_occurrence_indicators(
        column,
        min_occ=min_occ,
        normalization="association",
        clustering_method="louvain",
        directory=directory,
    )
