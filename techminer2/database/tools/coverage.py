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

>>> from techminer2.database.tools import Coverage
>>> (
...     Coverage()
...     .set_analysis_params(
...         field="author_keywords",
...     #
...     ).set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
--INFO-- Number of documents : 50
--INFO--   Documents with NA : 12
--INFO--  Efective documents : 38
   min_occ  cum_sum_documents  coverage  cum num items
0       31                 31   81.58 %              1
1        7                 33   86.84 %              2
2        4                 33   86.84 %              3
3        3                 35   92.11 %              7
4        2                 36   94.74 %             25
5        1                 38  100.00 %            148



"""
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ...internals.stopwords.load_user_stopwords import load_user_stopwords
from ..load.load__filtered_database import load__filtered_database
from .internals.set_field_param_mixin import SetFieldParamMixin


class Coverage(
    SetDatabaseFiltersMixin,
    SetFieldParamMixin,
):
    """:meta private:"""

    def __init__(self):
        self.database_params = DatabaseFilters()
        self.field = None

    def build(self):

        field = self.field

        stopwords = load_user_stopwords(self.database_params.root_dir)

        documents = load__filtered_database(**self.database_params.__dict__)

        documents = documents.reset_index()
        documents = documents[[field, "record_id"]]

        n_documents = len(documents)
        print(f"--INFO-- Number of documents : {n_documents}")
        print(
            "--INFO--   Documents with NA : " f"{n_documents - len(documents.dropna())}"
        )
        documents = documents.dropna()
        n_documents = len(documents)
        print(f"--INFO--  Efective documents : {n_documents}")

        documents = documents.assign(num_documents=1)
        documents[field] = documents[field].str.split("; ")
        documents = documents.explode(field)

        documents = documents[~documents[field].isin(stopwords)]

        documents = documents.groupby(by=[field]).agg(
            {"num_documents": "count", "record_id": list}
        )
        documents = documents.sort_values(by=["num_documents"], ascending=False)

        documents = documents.reset_index()

        documents = documents.groupby(by="num_documents", as_index=False).agg(
            {"record_id": list, field: list}
        )

        documents = documents.sort_values(by=["num_documents"], ascending=False)
        documents["record_id"] = documents.record_id.map(
            lambda x: [term for sublist in x for term in sublist]
        )

        documents = documents.assign(cum_sum_documents=documents.record_id.cumsum())
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
        documents = documents.assign(cum_sum_items=documents.cum_sum_items.map(set))
        documents = documents.assign(cum_sum_items=documents.cum_sum_items.map(len))

        documents.drop("record_id", axis=1, inplace=True)
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
