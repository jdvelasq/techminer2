"""
Column coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> column_coverage(directory, column="author_keywords").head(10) # doctest: +ELLIPSIS
20...
20...
20...
   min_occ  cum_sum_documents coverage  cum num items
0      977                977  59.25 %              1
1      279               1192  72.29 %              2
2      164               1206  73.14 %              3
3       87               1213  73.56 %              4
4       77               1224  74.23 %              5
5       72               1230  74.59 %              6
6       61               1233  74.77 %              7
7       60               1240  75.20 %              8
8       57               1244  75.44 %              9
9       56               1251  75.86 %             10

"""

from .utils import load_filtered_documents, load_stopwords, logging


def column_coverage(directory, column, sep="; "):

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
