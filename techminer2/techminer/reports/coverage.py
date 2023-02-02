"""
Coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.


>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.reports.coverage(
...     "author_keywords",
...     directory=directory,
... ).head(10)
--INFO-- Number of documents : 52
--INFO-- Documents with NA: 11
--INFO-- Efective documents : 52
   min_occ  cum_sum_documents coverage  cum num items
0       28                 28  53.85 %              1
1       12                 28  53.85 %              2
2        7                 33  63.46 %              4
3        5                 34  65.38 %              5
4        4                 37  71.15 %              8
5        3                 38  73.08 %             13
6        2                 39  75.00 %             26
7        1                 41  78.85 %            144


"""

import sys

from ..._lib._load_stopwords import load_stopwords
from ..._lib._read_records import read_records


def coverage(
    column,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Coverage of terms in a column discarding stopwords."""

    stopwords = load_stopwords(directory)

    documents = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    documents = documents.reset_index()
    documents = documents[[column, "article"]]

    n_documents = len(documents)
    sys.stdout.write(f"--INFO-- Number of documents : {n_documents}\n")
    sys.stdout.write(
        f"--INFO-- Documents with NA: {n_documents - len(documents.dropna())}\n"
    )

    documents = documents.dropna()
    sys.stdout.write(f"--INFO-- Efective documents : {n_documents}\n")

    documents = documents.assign(num_documents=1)
    documents[column] = documents[column].str.split("; ")
    documents = documents.explode(column)

    documents = documents[~documents[column].isin(stopwords)]

    documents = documents.groupby(by=[column]).agg(
        {"num_documents": "count", "article": list}
    )
    documents = documents.sort_values(by=["num_documents"], ascending=False)

    documents = documents.reset_index()

    documents = documents.groupby(by="num_documents", as_index=False).agg(
        {"article": list, column: list}
    )

    documents = documents.sort_values(by=["num_documents"], ascending=False)
    documents["article"] = documents.article.map(
        lambda x: [term for sublist in x for term in sublist]
    )

    documents = documents.assign(cum_sum_documents=documents.article.cumsum())
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

    documents.drop("article", axis=1, inplace=True)
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
