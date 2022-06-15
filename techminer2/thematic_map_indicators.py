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
adoption                             4                65  ...   0.533333  0.021741
artificial intelligence              6                30  ...   0.555556  0.025306
bank                                12               185  ...   0.588235  0.020175
bitcoin                              3                 7  ...   0.519481  0.016778
blockchain                          17               149  ...   0.625000  0.032010
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
