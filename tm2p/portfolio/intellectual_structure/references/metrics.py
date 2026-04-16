"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import ItemOrderBy
    >>> from tm2p.analyze.ref import Metrics
    >>> df = (
    ...     Metrics()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.GCS)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                                                                                                              REF  LCS
    0                                                                                                 Arner DW, 2017, NW J INT LAW BUS, V37, P371   50
    1                                                           Anagnostopoulos I, 2018, J ECON BUS, V100, P7, DOI 10.1016/j.jeconbus.2018.07.003   31
    2                                                                  Butler T, 2019, PALGR ST DIG BUS ENA, P85, DOI 10.1007/978-3-030-02330-0_6   21
    3  Arner DW, 2015, SSRN Electronic Journal, DOI [10.2139/ssrn.2676553, DOI 10.2139/SSRN.2676553, 10.2139/ssrn.2676553, 10.2139/ ssrn.2676553]   15
    4                                                                                                      Baxter LG, 2016, DUKE LAW J, V66, P567   14
    5                                                                   Kavassalis P, 2018, J RISK FINANC, V19, P39, DOI 10.1108/JRF-07-2017-0111   13
    6                                                                 Currie WL, 2018, J INF TECHNOL-UK, V33, P304, DOI 10.1057/s41265-017-0047-5   12
    7                                                                                                  Bamberger KA, 2010, TEX LAW REV, V88, P669   11
    8                                                                   Grassi L, 2022, J IND BUS ECON, V49, P441, DOI 10.1007/s40812-022-00226-0   10
    9                                                                    Buckley RP, 2020, J BANK REGUL, V21, P26, DOI 10.1057/s41261-019-00104-1   10


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = load_filtered_main_csv_zip(params=self.params)
        series = df[Field.GCR_WOS_FORMAT.value].dropna()
        series = series.str.split("; ").explode()
        series = series.str.strip()
        series = series.value_counts()

        result = pd.DataFrame(
            {
                "REF": series.index,
                "LCS": series.values,
            }
        )

        top_n = self.params.top_n if self.params.top_n else len(result)
        result = result.head(top_n)

        return result
