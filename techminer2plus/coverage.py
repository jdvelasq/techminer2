# flake8: noqa
"""
.. _coverage:

Coverage
===============================================================================

Computes coverage of terms in a column discarding stopwords.


>>> root_dir = "data/regtech/"

>>> import techminer2plus as tm2p
>>> tm2p.Records(root_dir=root_dir).coverage("author_keywords")
--INFO-- Number of documents : 52
--INFO--   Documents with NA : 11
--INFO--  Efective documents : 41
   min_occ  cum_sum_documents  coverage  cum num items
0       28                 28   68.29 %              1
1       12                 28   68.29 %              2
2        7                 33   80.49 %              4
3        5                 36   87.80 %              6
4        4                 39   95.12 %              9
5        3                 39   95.12 %             13
6        2                 39   95.12 %             25
7        1                 41  100.00 %            143


"""
from .stopwords_lib import load_stopwords


# pylint: disable=too-few-public-methods
class Coverage:
    """Computes the terms coverage of documents based on the OCC value."""

    root_dir: str

    def __init__(self):
        """Constructor"""

        self.stopwords = None

    def coverage(self, column):
        """Computes the terms coverage of documents based on the OCC value."""

        self.__load_stopwords()
        records = self.read_records()  # pylint: disable=no-member

        records = records.reset_index()
        records = records[[column, "article"]]

        n_raw_documents = len(records)
        records = records.dropna()
        n_documents = len(records)
        n_na_documents = n_raw_documents - n_documents

        print(f"--INFO-- Number of documents : {n_raw_documents}")
        print(f"--INFO--   Documents with NA : {n_na_documents}")
        print(f"--INFO--  Efective documents : {n_documents}")

        records = records.assign(num_documents=1)
        records[column] = records[column].str.split("; ")
        records = records.explode(column)
        records = records[~records[column].isin(self.stopwords)]
        records = records.groupby(by=[column]).agg(
            {"num_documents": "count", "article": list}
        )
        records = records.sort_values(by=["num_documents"], ascending=False)

        records = records.reset_index()

        records = records.groupby(by="num_documents", as_index=False).agg(
            {"article": list, column: list}
        )

        records = records.sort_values(by=["num_documents"], ascending=False)
        records["article"] = records.article.map(
            lambda x: [term for sublist in x for term in sublist]
        )

        records = records.assign(cum_sum_documents=records.article.cumsum())
        records = records.assign(
            cum_sum_documents=records.cum_sum_documents.map(set)
        )
        records = records.assign(
            cum_sum_documents=records.cum_sum_documents.map(len)
        )

        records = records.assign(
            coverage=records.cum_sum_documents.map(
                lambda x: f"{100 * x / n_documents:5.2f} %"
            )
        )

        records = records.assign(cum_sum_items=records[column].cumsum())
        records = records.assign(cum_sum_items=records.cum_sum_items.map(set))
        records = records.assign(cum_sum_items=records.cum_sum_items.map(len))

        records.drop("article", axis=1, inplace=True)
        records.drop(column, axis=1, inplace=True)

        records = records.rename(
            columns={
                "num_documents": "min_occ",
                "cum_sum": "cum num documents",
                "cum_sum_items": "cum num items",
            }
        )
        records = records.reset_index(drop=True)

        return records

    def __load_stopwords(self):
        self.stopwords = load_stopwords(self.root_dir)


# def coverage(
#     field,
#     # Database params:
#     root_dir="./",
#     database="main",
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """
#     Coverage of terms in a column discarding stopwords.

#     Args:
#         field (str): Database field to be used to extract the items.
#         root_dir (str): Root directory.
#         database (str): Database name.
#         year_filter (tuple, optional): Year database filter. Defaults to None.
#         cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
#         **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

#     Returns:
#         None.

#     """

#     stopwords = load_stopwords(root_dir)

#     documents = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     documents = documents.reset_index()
#     documents = documents[[field, "article"]]

#     n_documents = len(documents)
#     sys.stdout.write(f"--INFO-- Number of documents : {n_documents}\n")
#     sys.stdout.write(
#         "--INFO-- Documents with NA: "
#         f"{n_documents - len(documents.dropna())}\n"
#     )

#     documents = documents.dropna()
#     sys.stdout.write(f"--INFO-- Efective documents : {n_documents}\n")

#     documents = documents.assign(num_documents=1)
#     documents[field] = documents[field].str.split("; ")
#     documents = documents.explode(field)

#     documents = documents[~documents[field].isin(stopwords)]

#     documents = documents.groupby(by=[field]).agg(
#         {"num_documents": "count", "article": list}
#     )
#     documents = documents.sort_values(by=["num_documents"], ascending=False)

#     documents = documents.reset_index()

#     documents = documents.groupby(by="num_documents", as_index=False).agg(
#         {"article": list, field: list}
#     )

#     documents = documents.sort_values(by=["num_documents"], ascending=False)
#     documents["article"] = documents.article.map(
#         lambda x: [term for sublist in x for term in sublist]
#     )

#     documents = documents.assign(cum_sum_documents=documents.article.cumsum())
#     documents = documents.assign(
#         cum_sum_documents=documents.cum_sum_documents.map(set)
#     )
#     documents = documents.assign(
#         cum_sum_documents=documents.cum_sum_documents.map(len)
#     )

#     documents = documents.assign(
#         coverage=documents.cum_sum_documents.map(
#             lambda x: f"{100 * x / n_documents:5.2f} %"
#         )
#     )

#     documents = documents.assign(cum_sum_items=documents[field].cumsum())
#     documents = documents.assign(
#         cum_sum_items=documents.cum_sum_items.map(set)
#     )
#     documents = documents.assign(
#         cum_sum_items=documents.cum_sum_items.map(len)
#     )

#     documents.drop("article", axis=1, inplace=True)
#     documents.drop(field, axis=1, inplace=True)

#     documents = documents.rename(
#         columns={
#             "num_documents": "min_occ",
#             "cum_sum": "cum num documents",
#             "cum_sum_items": "cum num items",
#         }
#     )
#     documents = documents.reset_index(drop=True)

#     return documents
