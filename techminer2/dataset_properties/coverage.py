# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.

>>> from techminer2.dataset_properties import coverage
>>> coverage(
...     #
...     # PARAMS:
...     field="author_keywords",
...     #
...     # DATABASE_PARAMS
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- Number of documents : 52
--INFO--   Documents with NA : 11
--INFO--  Efective documents : 41
   min_occ  cum_sum_documents  coverage  cum num items
0       28                 28   68.29 %              1
1       12                 28   68.29 %              2
2        7                 33   80.49 %              4
3        5                 36   87.80 %              6
4        4                 39   95.12 %              9
5        3                 39   95.12 %             14
6        2                 39   95.12 %             25
7        1                 41  100.00 %            139



"""
from .._read_records import read_records
from .._stopwords_lib import load_stopwords


def coverage(
    field,
    #
    # DATABASE_PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
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

    :meta private:
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
    print(f"--INFO-- Number of documents : {n_documents}")
    print("--INFO--   Documents with NA : " f"{n_documents - len(documents.dropna())}")
    documents = documents.dropna()
    n_documents = len(documents)
    print(f"--INFO--  Efective documents : {n_documents}")

    documents = documents.assign(num_documents=1)
    documents[field] = documents[field].str.split("; ")
    documents = documents.explode(field)

    documents = documents[~documents[field].isin(stopwords)]

    documents = documents.groupby(by=[field]).agg({"num_documents": "count", "article": list})
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
    documents = documents.assign(cum_sum_documents=documents.cum_sum_documents.map(set))
    documents = documents.assign(cum_sum_documents=documents.cum_sum_documents.map(len))

    documents = documents.assign(
        coverage=documents.cum_sum_documents.map(lambda x: f"{100 * x / n_documents:5.2f} %")
    )

    documents = documents.assign(cum_sum_items=documents[field].cumsum())
    documents = documents.assign(cum_sum_items=documents.cum_sum_items.map(set))
    documents = documents.assign(cum_sum_items=documents.cum_sum_items.map(len))

    documents.drop("article", axis=1, inplace=True)
    documents.drop(field, axis=1, inplace=True)
    documents = documents.reset_index(drop=True)

    documents = documents.rename(
        columns={
            "num_documents": "min_occ",
            "cum_sum": "cum num documents",
            "cum_sum_items": "cum num items",
        }
    )

    return documents
