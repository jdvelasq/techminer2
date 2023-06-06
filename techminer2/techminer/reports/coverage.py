# flake8: noqa
"""
Coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.


>>> root_dir = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.reports.coverage(
...     "author_keywords",
...     root_dir=root_dir,
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

from ...load_utils import load_stopwords
from ...record_utils import read_records


def coverage(
    field,
    root_dir="./",
    database="documents",
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """
    Coverage of terms in a column discarding stopwords.

    Args:
        field (str): Database field to be used to extract the items.
        root_dir (str): Root directory.
        database (str): Database name.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        None.

    """

    stopwords = load_stopwords(root_dir)

    documents = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    documents = documents.reset_index()
    documents = documents[[field, "article"]]

    n_documents = len(documents)
    sys.stdout.write(f"--INFO-- Number of documents : {n_documents}\n")
    sys.stdout.write(
        "--INFO-- Documents with NA: "
        f"{n_documents - len(documents.dropna())}\n"
    )

    documents = documents.dropna()
    sys.stdout.write(f"--INFO-- Efective documents : {n_documents}\n")

    documents = documents.assign(num_documents=1)
    documents[field] = documents[field].str.split("; ")
    documents = documents.explode(field)

    documents = documents[~documents[field].isin(stopwords)]

    documents = documents.groupby(by=[field]).agg(
        {"num_documents": "count", "article": list}
    )
    documents = documents.sort_values(by=["num_documents"], ascending=False)

    documents = documents.reset_index()

    documents = documents.groupby(by="num_documents", as_index=False).agg(
        {"article": list, field: list}
    )

    documents = documents.sort_values(by=["num_documents"], ascending=False)
    documents["article"] = documents.article.map(
        lambda x: [term for sublist in x for term in sublist]
    )

    documents = documents.assign(cum_sum_documents=documents.article.cumsum())
    documents = documents.assign(
        cum_sum_documents=documents.cum_sum_documents.map(set)
    )
    documents = documents.assign(
        cum_sum_documents=documents.cum_sum_documents.map(len)
    )

    documents = documents.assign(
        coverage=documents.cum_sum_documents.map(
            lambda x: f"{100 * x / n_documents:5.2f} %"
        )
    )

    documents = documents.assign(cum_sum_items=documents[field].cumsum())
    documents = documents.assign(
        cum_sum_items=documents.cum_sum_items.map(set)
    )
    documents = documents.assign(
        cum_sum_items=documents.cum_sum_items.map(len)
    )

    documents.drop("article", axis=1, inplace=True)
    documents.drop(field, axis=1, inplace=True)

    documents = documents.rename(
        columns={
            "num_documents": "min_occ",
            "cum_sum": "cum num documents",
            "cum_sum_items": "cum num items",
        }
    )
    documents = documents.reset_index(drop=True)

    return documents
