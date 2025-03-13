# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Dataframe
===============================================================================

This module demonstrates how to create a DataFrame using the Bradford's Law metrics
with the DataFrame class. The process involves configuring the database parameters.


Example:
    >>> from techminer2.database.metrics.bradford_law import DataFrame

    >>> generator = (
    ...     DataFrame()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ... )
    >>> df = generator.run()
    >>> df
       Num Sources        %  ...  Tot Documents Bradford's Group
    0            1   2.44 %  ...          6.0 %                1
    1            7  17.07 %  ...         34.0 %                2
    2           33  80.49 %  ...        100.0 %                3
    <BLANKLINE>
    [3 rows x 9 columns]

"""
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals.io import internal__load_filtered_records_from_database


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_filtered_records(self):
        self.records = internal__load_filtered_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def internal__compute_num_docs_published_by_source(self):

        self.records["num_documents"] = 1

        sources = self.records.groupby("source_title", as_index=True).agg(
            {
                "num_documents": "sum",
            }
        )
        sources = sources[["num_documents"]]
        sources = sources.groupby(["num_documents"]).size()
        w = [str(round(100 * a / sum(sources), 2)) + " %" for a in sources]
        sources = pd.DataFrame(
            {
                "Num Sources": sources.tolist(),
                "%": w,
                "Documents published": sources.index,
            }
        )

        sources = sources.sort_values(["Documents published"], ascending=False)

        self.sources = sources

    # -------------------------------------------------------------------------
    def internal__compute_bradors_zone_groups(self):

        sources = self.sources.copy()

        sources.loc[:, "Acum Num Sources"] = sources["Num Sources"].cumsum()
        sources["% Acum"] = [
            str(round(100 * a / sum(sources["Num Sources"]), 2)) + " %"
            for a in sources["Acum Num Sources"]
        ]

        sources["Tot Documents published"] = (
            sources["Num Sources"] * sources["Documents published"]
        )
        sources["Num Documents"] = sources["Tot Documents published"].cumsum()
        sources["Tot Documents"] = sources["Num Documents"].map(
            lambda w: str(round(w / sources["Num Documents"].max() * 100, 2)) + " %"
        )

        bradford1 = int(len(self.records) / 3)
        bradford2 = 2 * bradford1

        sources["Bradford's Group"] = sources["Num Documents"].map(
            lambda w: 3 if w > bradford2 else (2 if w > bradford1 else 1)
        )

        sources = sources[
            [
                "Num Sources",
                "%",
                "Acum Num Sources",
                "% Acum",
                "Documents published",
                "Tot Documents published",
                "Num Documents",
                "Tot Documents",
                "Bradford's Group",
            ]
        ]

        sources = sources.reset_index(drop=True)

        self.sources = sources

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__load_filtered_records()
        self.internal__compute_num_docs_published_by_source()
        self.internal__compute_bradors_zone_groups()

        return self.sources
