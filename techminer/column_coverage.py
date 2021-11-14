"""
Column coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> column_coverage(directory, column="author_keywords").head(10)
2021-11-14 14:48:34 - INFO - Number of documents : 1301
2021-11-14 14:48:34 - INFO - Documents with NA: 1122
2021-11-14 14:48:34 - INFO - Efective documents : 1301
   min_occ  total num documents coverage
0      132                  131  10.07 %
1       72                  256  19.68 %
2       50                  289  22.21 %
3       48                  324  24.90 %
4       44                  353  27.13 %
5       40                  367  28.21 %
6       39                  400  30.75 %
7       38                  425  32.67 %
8       33                  451  34.67 %
9       30                  485  37.28 %

"""

from .utils import load_filtered_documents, load_stopwords, logging


def column_coverage(directory, column, sep="; "):

    stopwords = load_stopwords(directory)

    documents = load_filtered_documents(directory)
    documents = documents[[column, "document_id"]]

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
        {"num_documents": "count", "document_id": list}
    )
    documents = documents.sort_values(by=["num_documents"], ascending=False)

    documents = documents.groupby(by="num_documents", as_index=False).agg(
        {"document_id": list}
    )

    documents = documents.sort_values(by=["num_documents"], ascending=False)
    documents["document_id"] = documents.document_id.map(
        lambda x: [term for sublist in x for term in sublist]
    )

    documents = documents.assign(cum_sum=documents.document_id.cumsum())
    documents = documents.assign(cum_sum=documents.cum_sum.map(set))
    documents = documents.assign(cum_sum=documents.cum_sum.map(len))

    documents = documents.assign(
        coverage=documents.cum_sum.map(
            lambda x: "{:5.2f} %".format(100 * x / n_documents)
        )
    )

    documents.drop("document_id", axis=1, inplace=True)
    documents = documents.rename(
        columns={"num_documents": "min_occ", "cum_sum": "total num documents"}
    )
    documents = documents.reset_index(drop=True)

    return documents
