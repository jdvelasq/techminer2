"""
Thematic Map / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> thematic_map_indicators(
...     'author_keywords', min_occ=4, directory=directory
... ).head()
                        num_documents  global_citations  ...  closeness  pagerank
node                                                     ...                     
bank                                5                12  ...   0.636364  0.106303
blockchain                          6                 9  ...   0.636364  0.126858
covid-19                            6                 8  ...   0.583333  0.109351
financial inclusion                10                14  ...   0.636364  0.094269
financial technologies             12                32  ...   0.700000  0.131281
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
