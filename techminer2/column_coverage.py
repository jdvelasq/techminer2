"""
Column Coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> column_coverage("author_keywords", directory=directory).head(10)
- INFO - Number of documents : 248
- INFO - Documents with NA: 202
- INFO - Efective documents : 248
   min_occ  cum_sum_documents coverage  cum num items
0      139                139  56.05 %              1
1       28                153  61.69 %              2
2       17                158  63.71 %              4
3       13                162  65.32 %              6
4       12                164  66.13 %              7
5       11                166  66.94 %              8
6        8                174  70.16 %             13
7        7                174  70.16 %             17
8        6                177  71.37 %             24
9        5                179  72.18 %             29

"""

from . import logging
from .load_filtered_documents import load_filtered_documents
from .load_stopwords import load_stopwords


def column_coverage(column, sep="; ", directory="./"):

    stopwords = load_stopwords(directory)

    documents = load_filtered_documents(directory)
    documents = documents.reset_index()
    documents = documents[[column, "record_no"]]

    n_documents = len(documents)
    logging.info("Number of documents : {}".format(n_documents))
    logging.info("Documents with NA: {}".format(len(documents.dropna())))

    documents = documents.dropna()
    logging.info("Efective documents : {}".format(n_documents))

    documents = documents.assign(num_documents=1)
    documents[column] = documents[column].str.split("; ")
    documents = documents.explode(column)

    documents = documents[~documents[column].isin(stopwords)]

    documents = documents.groupby(by=[column]).agg(
        {"num_documents": "count", "record_no": list}
    )
    documents = documents.sort_values(by=["num_documents"], ascending=False)

    documents = documents.reset_index()

    documents = documents.groupby(by="num_documents", as_index=False).agg(
        {"record_no": list, column: list}
    )

    documents = documents.sort_values(by=["num_documents"], ascending=False)
    documents["record_no"] = documents.record_no.map(
        lambda x: [term for sublist in x for term in sublist]
    )

    documents = documents.assign(cum_sum_documents=documents.record_no.cumsum())
    documents = documents.assign(cum_sum_documents=documents.cum_sum_documents.map(set))
    documents = documents.assign(cum_sum_documents=documents.cum_sum_documents.map(len))

    documents = documents.assign(
        coverage=documents.cum_sum_documents.map(
            lambda x: "{:5.2f} %".format(100 * x / n_documents)
        )
    )

    documents = documents.assign(cum_sum_items=documents[column].cumsum())
    documents = documents.assign(cum_sum_items=documents.cum_sum_items.map(set))
    documents = documents.assign(cum_sum_items=documents.cum_sum_items.map(len))

    documents.drop("record_no", axis=1, inplace=True)
    documents.drop(column, axis=1, inplace=True)

    documents = documents.rename(
        columns={
            "num_documents": "min_occ",
            "cum_sum": "cum num documents",
            "cum_sum_items": "cum num items",
        }
    )
    documents = documents.reset_index(drop=True)

    return documents
