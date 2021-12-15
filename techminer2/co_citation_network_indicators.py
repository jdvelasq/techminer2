"""
Co-citation Network / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_citation_network_indicators(directory=directory).head()
           num_documents  global_citations  ...  closeness  pagerank
node                                        ...                     
1989-0000          25830                14  ...   0.700000  0.019213
2000-0000           9760                 7  ...   0.620253  0.013109
2003-0002          16860                 9  ...   0.628205  0.015167
2009-0013            876                 9  ...   0.604938  0.011282
2013-0009            553                 6  ...   0.550562  0.005362
<BLANKLINE>
[5 rows x 6 columns]

"""

from .co_citation_matrix import co_citation_matrix
from .network import network
from .network_indicators import network_indicators


def co_citation_network_indicators(
    top_n=50,
    clustering_method="louvain",
    directory="./",
):

    matrix = co_citation_matrix(
        top_n=top_n,
        directory=directory,
    )

    network_ = network(
        matrix,
        clustering_method=clustering_method,
    )

    return network_indicators(network_)
