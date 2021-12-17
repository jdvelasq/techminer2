"""
Collaboration Network / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> collaboration_network_indicators('authors', min_occ=2, directory=directory).head()
            num_documents  global_citations  ...  closeness  pagerank
node                                         ...                     
Arqawi S                2                 5  ...   0.027027  0.034904
Bernards N              2                35  ...   0.000000  0.005236
Budi I                  2                 8  ...   0.054054  0.034904
Daragmeh A              2                 3  ...   0.027027  0.034904
Dincer H                2                15  ...   0.054054  0.038757
<BLANKLINE>
[5 rows x 6 columns]

"""
from .co_occurrence_network_indicators import co_occurrence_network_indicators


def collaboration_network_indicators(
    column,
    min_occ=2,
    normalization="association",
    clustering_method="louvain",
    directory="./",
):

    if column not in ["authors", "institutions", "countries"]:
        raise ValueError("The column must be 'authors', 'institutions' or 'countries'")

    return co_occurrence_network_indicators(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        directory=directory,
    )
