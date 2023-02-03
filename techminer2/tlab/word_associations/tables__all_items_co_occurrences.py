"""
All Items (Co-Occurrences)
===============================================================================




>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> tlab.word_associations.tables__all_items_co_occurrences(
...     criterion='author_keywords',
...     directory=directory,
... ).head(5)
              row                        column  OCC
0  regtech 28:329                regtech 28:329   28
1  regtech 28:329                fintech 12:249   12
2  regtech 28:329  regulatory technology 07:037    2
3  regtech 28:329             compliance 07:030    7
4  regtech 28:329             regulation 05:164    4


"""
from ... import vantagepoint


def tables__all_items_co_occurrences(
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

    return vantagepoint.analyze.matrix.co_occ_matrix_list(
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
