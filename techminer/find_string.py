"""
Find string
===============================================================================

Finds a string in the terms of a column of a document collection.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> find_string("author_keywords", contains='fintech',directory=directory).head()
0                       b2b fintech
1          bank fintech partnership
2                   banking-fintech
3    bermuda fintech innovation hub
4             bermuda fintech story
Name: author_keywords, dtype: object

"""


from .utils import load_filtered_documents


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
    documents = load_filtered_documents(directory)
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
    documents = documents.drop_duplicates()
    documents = documents.sort_values(ascending=True)
    documents = documents.reset_index(drop=True)
    return documents
