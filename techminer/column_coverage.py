"""
Column coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> column_coverage("author_keywords", directory=directory).head(10)
- INFO - Number of documents : 826
- INFO - Documents with NA: 620
- INFO - Efective documents : 826
   min_occ  cum_sum_documents coverage  cum num items
0      428                428  51.82 %              1
1       70                468  56.66 %              2
2       44                477  57.75 %              3
3       41                485  58.72 %              4
4       39                488  59.08 %              5
5       37                493  59.69 %              6
6       26                497  60.17 %              7
7       24                499  60.41 %              8
8       23                503  60.90 %              9
9       22                513  62.11 %             11

"""

from .utils import load_filtered_documents, load_stopwords, logging


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
