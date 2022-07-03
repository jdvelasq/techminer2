"""
Word Associations for a Item
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"

>>> word_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
... ).head()


"""
from ._read_records import read_records


def word_associations_for_a_item(
    item,
    column,
    top_n=10,
    max_occ=None,
    min_occ=None,
    directory="./",
    database="documents",
):
    records = read_records(
        directory=directory,
        database="documents",
        use_filter=True,
    )
    records = records[[column]]
    records = records.assign(COL=records[column])
    records = records.dropna()

    records = records["COL"].str.split(";")
    records = records.explode("COL")
    records["COL"] = records["COL"].str.strip()

    records = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()

    records = records[(records[column] == item) | (records["COL"] == item)]
