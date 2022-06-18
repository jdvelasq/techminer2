"""
Thematic Map / Summarization
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> thematic_map_summarization(
...     'author_keywords', 
...     min_occ=4, 
...     n_keywords=5,
...     n_phrases=3,
...     directory=directory,
... )
- INFO - Generating data/reports/keywords_summarization_CL_00.txt
- INFO - Generating data/reports/keywords_summarization_CL_01.txt

"""


from .co_occurrence_network_summarization import co_occurrence_network_summarization


def thematic_map_summarization(
    column,
    min_occ=2,
    max_occ=None,
    n_keywords=5,
    n_phrases=10,
    directory="./",
):

    return co_occurrence_network_summarization(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization="association",
        clustering_method="louvain",
        manifold_method=None,
        n_keywords=n_keywords,
        n_phrases=n_phrases,
        directory=directory,
    )
