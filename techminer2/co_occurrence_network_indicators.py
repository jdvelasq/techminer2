"""
Co-occurrence Network / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> co_occurrence_network_indicators(
...     'author_keywords',
...     min_occ=2,
...     directory=directory,
... ).head()
                         num_documents  global_citations  ...  closeness  pagerank
node                                                      ...                     
adoption                             4                65  ...   0.505792  0.005603
africa                               2                 8  ...   0.490637  0.003784
api                                  2                 5  ...   0.505792  0.004477
artificial intelligence              6                30  ...   0.519841  0.008282
attitude                             2                 3  ...   0.385294  0.005405
<BLANKLINE>
[5 rows x 6 columns]


"""

from .co_occurrence_matrix import co_occurrence_matrix
from .network_api.network import network
from .network_api.network_indicators import network_indicators


def co_occurrence_network_indicators(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        directory=directory,
    )

    network_ = network(
        matrix=coc_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_indicators(network_)
