"""
Associations for a Item
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> associations_for_a_item(
...     'regtech',
...     'author_keywords',
...     directory=directory,
... ).head()
author_keywords
fintech 42:406                    42
blockchain 18:109                 17
compliance 12:020                 12
artificial intelligence 13:065    10
financial regulation 08:091        8
Name: OCC, dtype: int64

"""
from .associations_for_all_items import associations_for_all_items


def associations_for_a_item(
    item,
    column,
    directory="./",
    database="documents",
):
    """Computes the co-occurrence matrix for a given column."""

    word_associations = associations_for_all_items(
        column=column,
        directory=directory,
        database=database,
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
    word_associations.columns = [column, "OCC"]
    word_associations = word_associations.set_index(column)

    return word_associations.OCC.sort_values(ascending=False)
