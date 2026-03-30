"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.anal.rpys import Metrics
    >>> (
    ...     Metrics()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/wos/")
    ...     .run()
    ... ).head()
          N_GCR  MEDIAN
    2016      1    -1.0
    2017      6    -6.0
    2018     13   -13.0
    2019     12   -12.0
    2020     19    -7.0


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

        median = indicator.loc[:, "N_GCR"].rolling(window=5).median().fillna(0)

        indicator = indicator.assign(MEDIAN=median)

        indicator["MEDIAN"] = indicator["MEDIAN"] - indicator["N_GCR"]

        return indicator
