# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Summary Sheet
===============================================================================

Example:
    >>> from techminer2.database.tools import SummarySheet
    >>> result = (
    ...     SummarySheet()
    ...     #
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... )
    >>> result.head(10)
                           column  number of records coverage (%)
    0           abbr_source_title                 50      100.00%
    1                    abstract                 48       96.00%
    2  abstract_nouns_and_phrases                 48       96.00%
    3                affiliations                 49       98.00%
    4           author_full_names                 50      100.00%
    5             author_keywords                 38       76.00%
    6                     authors                 50      100.00%
    7                  authors_id                 50      100.00%
    8   authors_with_affiliations                 49       98.00%
    9            cleaned_abstract                 48       96.00%


"""
import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals.io import internal__load_filtered_records_from_database


class SummarySheet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        records = internal__load_filtered_records_from_database(params=self.params)

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
