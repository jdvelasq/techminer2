"""
Find String
===============================================================================

Finds a string in the terms of a column of a document collection.

>>> from techminer2 import *
>>> directory = "data/"
>>> find_string("author_keywords", contains='fintech', directory=directory).head(10)
fintech                          139
fintech-innovations                5
fintech application                3
fintech companies                  2
fintech continuance intention      2
fintech development                2
fintech ecosystem                  2
fintech platform                   2
islamic fintech                    2
characteristics of fintech         1
Name: author_keywords, dtype: int64

"""


from ._read_records import read_filtered_records


def find_string(
    column,
    sep="; ",
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
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
    documents = read_filtered_records(directory)
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
