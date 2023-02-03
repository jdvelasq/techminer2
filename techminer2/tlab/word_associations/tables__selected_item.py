"""
Selected Item
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> tlab.word_associations.tables__selected_item(
...     item='regtech',
...     criterion='author_keywords',
...     directory=directory,
... ).head()
author_keywords
fintech 12:249               12
compliance 07:030             7
regulation 05:164             4
financial services 04:168     3
suptech 03:004                3
Name: OCC, dtype: int64


"""
from .tables__all_items_co_occurrences import tables__all_items_co_occurrences


def tables__selected_item(
    item,
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
    """Computes the co-occurrence matrix for a given column."""

    word_associations = tables__all_items_co_occurrences(
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

    word_associations["row"] = word_associations["row"].str.split()
    word_associations["row"] = word_associations["row"].str[:-1]
    word_associations["row"] = word_associations["row"].str.join(" ")
    word_associations = word_associations[word_associations.row == item]

    word_associations["text"] = word_associations["column"].str.split()
    word_associations["text"] = word_associations["text"].str[:-1]
    word_associations["text"] = word_associations["text"].str.join(" ")
    word_associations = word_associations[word_associations.text != item]
    word_associations = word_associations[["column", "OCC"]]
    word_associations.columns = [criterion, "OCC"]
    word_associations = word_associations.set_index(criterion)

    return word_associations.OCC.sort_values(ascending=False)
