# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Summary Sheet
===============================================================================


## >>> from techminer2.prepare.database import SummarySheet
## >>> result = (
## ...     SummarySheet()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build()
## ... )
## >>> result.head()
                 column  number of terms coverage (%)
0     abbr_source_title               50         1.0%
1              abstract               48        0.96%
2  abstract_nlp_phrases               48        0.96%
3          affiliations               49        0.98%
4                art_no                6        0.12%



"""
import pandas as pd  # type: ignore

from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.read_filtered_database import read_filtered_database


class SummarySheet(
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.database_params = DatabaseParams()

    def build(self):

        records = read_filtered_database(**self.database_params.__dict__)

        #
        # Compute stats per column
        columns = sorted(records.columns)

        n_documents = len(records)

        report = pd.DataFrame({"column": columns})

        report["number of terms"] = [
            n_documents - records[col].isnull().sum() for col in columns
        ]

        report["coverage (%)"] = [
            f"{(n_documents - records[col].isnull().sum()) / n_documents:5.2}%"
            for col in columns
        ]

        return report
