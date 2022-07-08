"""
Co-occurrence Network / Summarization
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> co_occurrence_network_summarization(
...     'author_keywords', 
...     min_occ=4, 
...     n_keywords=5,
...     n_phrases=3,
...     directory=directory,
... )
- INFO - Generating data/reports/keywords_summarization_CL_00.txt
- INFO - Generating data/reports/keywords_summarization_CL_01.txt
- INFO - Generating data/reports/keywords_summarization_CL_02.txt
- INFO - Generating data/reports/keywords_summarization_CL_03.txt


"""

from .co_occurrence_network_communities import co_occurrence_network_communities
from .keywords_summarization import keywords_summarization


def co_occurrence_network_summarization(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    n_keywords=5,
    n_phrases=10,
    directory="./",
):

    cm = co_occurrence_network_communities(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
        directory=directory,
    )

    cm = cm.head(n_keywords).transpose()

    for row in cm.iterrows():

        list_of_keywords = []

        for word in row[1]:
            word = word.split(" ")
            word = word[:-1]
            word = " ".join(word)
            list_of_keywords.append(word)

        keywords_summarization(
            column=column,
            keywords=list_of_keywords,
            n_phrases=n_phrases,
            sufix="_" + row[0],
            directory=directory,
        )
