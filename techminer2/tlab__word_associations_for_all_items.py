"""
All Items (Co-Occurrences)
===============================================================================




>>> directory = "data/regtech/"

>>> from techminer2 import tlab__word_associations_for_all_items
>>> tlab__word_associations_for_all_items(
...     criterion='author_keywords',
...     directory=directory,
... ).head(10)
              row                          column  OCC
0  regtech 69:461                  regtech 69:461   69
1  regtech 69:461                  fintech 42:406   42
2  regtech 69:461               blockchain 18:109   17
3  regtech 69:461  artificial intelligence 13:065   10
4  regtech 69:461    regulatory technology 12:047    4
5  regtech 69:461               compliance 12:020   12
6  regtech 69:461     financial technology 09:032    5
7  regtech 69:461     financial regulation 08:091    8
8  regtech 69:461               regulation 06:120    5
9  regtech 69:461         machine learning 06:013    6


"""
from .vantagepoint.analyze.matrix.co_occ_matrix_list import co_occ_matrix_list


def tlab__word_associations_for_all_items(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes the co-occurrence matrix list."""

    return co_occ_matrix_list(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
