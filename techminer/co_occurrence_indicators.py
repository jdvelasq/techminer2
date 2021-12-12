"""
Co-occurrence Network / Indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_occurrence_indicators('author_keywords', min_occ=2, directory=directory).head()
                         num_documents  global_citations  ...  closeness  pagerank
node                                                      ...                     
adoption                             4                65  ...   0.507752  0.005644
africa                               2                 8  ...   0.492481  0.003803
api                                  2                 5  ...   0.505792  0.004509
artificial intelligence              6                30  ...   0.521912  0.008387
attitude                             2                 3  ...   0.385294  0.005414
<BLANKLINE>
[5 rows x 6 columns]


"""

from .co_occurrence_matrix import co_occurrence_matrix
from .network import network
from .network_indicators import network_indicators


def co_occurrence_indicators(
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
