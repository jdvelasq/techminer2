"""
Find String
===============================================================================

Finds a string in the terms of a column of a document collection.

>>> from techminer2 import *
>>> directory = "data/"

>>> find_string(
...     "author_keywords", 
...     contains='fintech', 
...     directory=directory,
... ).head(10)
fintech                   42
fintech credit             1
fintech crises             1
fintech regtech            1
fintech sustainability     1
Name: author_keywords, dtype: int64

"""
from ._read_records import read_records


def find_string(
    column,
    sep="; ",
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
    database="documents",
    use_filter=True,
):
    """
    Find string in documents

    :param directory: directory with documents
    :param column: column number
    :param sep: separator
    :param contains: string to find
    :param startswith: string to find
    :param endswith: string to find
    :return: list of strings
    """

    documents = read_records(
        directory=directory, database=database, use_filter=use_filter
    )
    documents.index = documents.record_no
    documents = documents[column]
    documents = documents.dropna()
    documents = documents.str.split(sep)
    documents = documents.explode()
    if contains is not None:
        documents = documents[documents.str.contains(contains)]
    elif startswith is not None:
        documents = documents[documents.str.startswith(startswith)]
    elif endswith is not None:
        documents = documents[documents.str.endswith(endswith)]
    else:
        raise ValueError("No filter provided")
    # ----< modified to return counts >--------------------------------------
    # documents = documents.drop_duplicates()
    # documents = documents.sort_values(ascending=True)
    # documents = documents.reset_index(drop=True)

    documents = documents.value_counts().to_frame()
    documents["_index_"] = documents.index
    documents = documents.sort_values(by=[column, "_index_"], ascending=[False, True])
    documents = documents[column]
    return documents
