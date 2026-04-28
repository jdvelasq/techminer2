"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.perform_metr.bradford import Metrics
    >>> df = (
    ...     Metrics()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
        N_SRC  CUM_N_SRC PERC_N_SRC PERC_CUM_N_SRC  N_DOCS  N_REC  CUM_N_REC PERC_CUM_N_REC  ZONE
    0       1          1     0.14 %         0.14 %      42     42         42         2.84 %     1
    1       1          2     0.14 %         0.29 %      40     40         82         5.54 %     1
    2       1          3     0.14 %         0.43 %      31     31        113         7.63 %     1
    3       1          4     0.14 %         0.57 %      28     28        141         9.52 %     1
    4       1          5     0.14 %         0.71 %      25     25        166        11.21 %     1
    5       1          6     0.14 %         0.86 %      21     21        187        12.63 %     1
    6       1          7     0.14 %         1.00 %      20     20        207        13.98 %     1
    7       1          8     0.14 %         1.14 %      17     17        224        15.12 %     1
    8       1          9     0.14 %         1.28 %      16     16        240        16.21 %     1
    9       4         13     0.57 %         1.85 %      15     60        300        20.26 %     1
    10      1         14     0.14 %         2.00 %      14     14        314        21.20 %     1
    11      3         17     0.43 %         2.43 %      13     39        353        23.84 %     1
    12      3         20     0.43 %         2.85 %      12     36        389        26.27 %     1
    13      1         21     0.14 %         3.00 %      10     10        399        26.94 %     1
    14      2         23     0.29 %         3.28 %       9     18        417        28.16 %     1
    15      4         27     0.57 %         3.85 %       8     32        449        30.32 %     1
    16      4         31     0.57 %         4.42 %       7     28        477        32.21 %     1
    17      9         40     1.28 %         5.71 %       6     54        531        35.85 %     2
    18     10         50     1.43 %         7.13 %       5     50        581        39.23 %     2
    19     23         73     3.28 %        10.41 %       4     92        673        45.44 %     2
    20     36        109     5.14 %        15.55 %       3    108        781        52.73 %     2
    21    108        217    15.41 %        30.96 %       2    216        997        67.32 %     3
    22    484        701    69.04 %       100.00 %       1    484       1481       100.00 %     3



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field

SRC_ISO4 = Field.SRC_ISO4.value


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = load_filtered_main_csv_zip(params=self.params)
        df["N_DOCS"] = 1
        metrics = df.groupby(SRC_ISO4, as_index=True).agg(
            {
                "N_DOCS": "sum",
            }
        )
        metrics = metrics[["N_DOCS"]]
        metrics = metrics.groupby(["N_DOCS"], as_index=False).size()
        metrics.columns = ["N_DOCS", "N_SRC"]  # type: ignore
        metrics = metrics.sort_values(by="N_DOCS", ascending=False)  # type: ignore
        metrics = metrics.reset_index(drop=True)  # type: ignore

        metrics["CUM_N_SRC"] = metrics["N_SRC"].cumsum()

        n_sources = metrics["N_SRC"].sum()

        metrics["PERC_N_SRC"] = metrics["N_SRC"].map(
            lambda x: f"{100 * x / n_sources:.2f} %"
        )
        metrics["PERC_CUM_N_SRC"] = metrics["CUM_N_SRC"].map(
            lambda x: f"{100 * x / n_sources:.2f} %"
        )

        metrics = metrics[
            ["N_SRC", "CUM_N_SRC", "PERC_N_SRC", "PERC_CUM_N_SRC", "N_DOCS"]
        ]

        metrics["N_REC"] = metrics["N_SRC"] * metrics["N_DOCS"]
        metrics["CUM_N_REC"] = metrics["N_REC"].cumsum()
        metrics["PERC_CUM_N_REC"] = metrics["CUM_N_REC"].map(
            lambda x: f"{100 * x / metrics['N_REC'].sum():.2f} %"
        )

        bradford1 = int(len(df) / 3)
        bradford2 = 2 * bradford1

        metrics["ZONE"] = metrics["CUM_N_REC"].map(
            lambda w: 3 if w > bradford2 else (2 if w > bradford1 else 1)
        )

        return metrics
