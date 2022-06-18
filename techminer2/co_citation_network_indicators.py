"""
Co-citation Network / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> co_citation_network_indicators(directory=directory).head()
                                                 num_documents  ...  pagerank
node                                                            ...          
Allen HJ et al, 2019, GEORGE WASHINGTON LAW REV             21  ...  0.008687
Alt R et al, 2018, ELECTRON MARK                            62  ...  0.017369
Anagnostopoulos I et al, 2018, J ECON BUS                   76  ...  0.024708
Anshari M et al, 2019, ENERGY PROCEDIA                      35  ...  0.014987
Arner DW et al, 2020, EUR BUS ORG LAW REV                   26  ...  0.019136
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
