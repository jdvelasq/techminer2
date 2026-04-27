"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.intellect_struct.rpys import Metrics
    >>> df = (
    ...     Metrics()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> df.head(50)
          N_GCR  MEDIAN   PEAK
    YEAR
    2006      5     0.0  False
    2007      5    -1.0  False
    2008      7     0.0   True
    2009     12     0.0  False
    2010     14     2.0   True
    2011     12    -2.0  False
    2012     17     3.0   True
    2013     14    -3.0  False
    2014     19     2.0  False
    2015     23     4.0   True
    2016     14    -9.0  False
    2017     27     0.0  False
    2018     32     4.0   True
    2019     28    -3.0  False
    2020     31    -1.0  False
    2021     49    10.0   True
    2022     55     7.0  False
    2023     39   -10.0  False
    2024     48     0.0  False
    2025     55    11.5   True
    2026     16   -32.0  False


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> pd.DataFrame:
        """:meta private:"""

        references = load_filtered_main_csv_zip(params=self.params)

        references = references[["YEAR"]]
        references = references.dropna()
        references_by_year = references["YEAR"].value_counts()

        year_min = references_by_year.index.min()
        year_max = references_by_year.index.max()
        years = list(range(year_min, year_max + 1))

        indicator: pd.DataFrame = pd.DataFrame(
            {
                "N_GCR": 0,
            },
            index=years,
        )

        indicator.loc[references_by_year.index, "N_GCR"] = references_by_year
        indicator = indicator.sort_index(axis=0, ascending=True)

        median = (
            indicator.loc[:, "N_GCR"]
            .rolling(window=5, center=True, min_periods=1)
            .median()
        )

        indicator.loc[:, "MEDIAN"] = indicator.loc[:, "N_GCR"] - median

        indicator.loc[:, "PEAK"] = False

        for index, row in indicator.iterrows():

            if index == year_min or index == year_max:
                continue

            if row["MEDIAN"] >= indicator.loc[index - 1, "MEDIAN"]:  # type: ignore
                if row["MEDIAN"] >= indicator.loc[index + 1, "MEDIAN"]:  # type: ignore
                    indicator.loc[index, "PEAK"] = True

        indicator.index.name = "YEAR"

        return indicator
