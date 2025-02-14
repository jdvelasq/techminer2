# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Summary Sheet
===============================================================================


>>> from techminer2.database.tools import SummarySheet
>>> result = (
...     SummarySheet()
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> result.head(10)
                      column  number of records coverage (%)
0          abbr_source_title                 50      100.00%
1                   abstract                 48       96.00%
2               affiliations                 49       98.00%
3          author_full_names                 50      100.00%
4            author_keywords                 38       76.00%
5                    authors                 50      100.00%
6                 authors_id                 50      100.00%
7  authors_with_affiliations                 50      100.00%
8                      coden                 12       24.00%
9            conference_code                  3        6.00%

"""
import pandas as pd  # type: ignore

from ...internals.mixins import ParamsMixin
from ..internals.io import internal__load_filtered_database


class SummarySheet(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        records = (
            internal__load_filtered_database()
            .update_params(**self.params.__dict__)
            .build()
        )

        #
        # Compute stats per column
        columns = sorted(records.columns)

        n_documents = len(records)

        report = pd.DataFrame({"column": columns})

        report["number of records"] = [
            n_documents - records[col].isnull().sum() for col in columns
        ]

        report["coverage (%)"] = [
            f"{100*(float(n_documents) - records[col].isnull().sum()) / n_documents:5.2f}%"
            for col in columns
        ]

        return report
