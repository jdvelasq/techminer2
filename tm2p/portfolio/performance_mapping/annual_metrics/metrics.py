"""
DataFrame
===============================================================================

Smoke tests:
    >>> from tm2p.analyze.annual_metrics.metrics import Metrics
    >>> df = (
    ...     Metrics()
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
          OCC  CUMUL_OCC  CITAB_YEAR   GCS  CUMUL_GCS    MEAN_GCS  MEAN_GCS_PER_YEAR  LCS  CUMUL_LCS  MEAN_LCS  MEAN_LCS_PER_YEAR
    YEAR
    2015    6          6          10   132        132   22.000000               2.20    0          0       0.0                0.0
    2016   18         24           9  1992       2124  110.666667              12.30    0          0       0.0                0.0
    2017   19         43           8  3743       5867  197.000000              24.62    0          0       0.0                0.0
    2018   18         61           7  6770      12637  376.111111              53.73    0          0       0.0                0.0
    2019   19         80           6  4906      17543  258.210526              43.04    0          0       0.0                0.0
    2020   20        100           5  5396      22939  269.800000              53.96    0          0       0.0                0.0
    2021   20        120           4  5637      28576  281.850000              70.46    0          0       0.0                0.0
    2022   20        140           3  5172      33748  258.600000              86.20    0          0       0.0                0.0
    2023   20        160           2  2750      36498  137.500000              68.75    0          0       0.0                0.0
    2024   20        180           1  1684      38182   84.200000              84.20    0          0       0.0                0.0


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip

from .column import Column

GCS = Column.GCS.value
LCS = Column.LCS.value
YEAR = Column.YEAR.value
OCC = Column.OCC.value
CUMUL_OCC = Column.CUMUL_OCC.value
CUMUL_LCS = Column.CUMUL_LCS.value
CITAB_YEAR = Column.CITAB_YEAR.value
MEAN_LCS_PER_YEAR = Column.MEAN_LCS_PER_YEAR.value
MEAN_GCS_PER_YEAR = Column.MEAN_GCS_PER_YEAR.value

MEAN_GCS = Column.MEAN_GCS.value
MEAN_LCS = Column.MEAN_LCS.value
CUMUL_GCS = Column.CUMUL_GCS.value


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def _select_columns(self, df):

        df = df.copy()

        columns = [
            YEAR,
            GCS,
            LCS,
        ]
        df = df[columns]
        df[OCC] = 1
        df[YEAR] = df[YEAR].astype(int)

        return df

    def _group_by_year_and_sort(self, df):

        df = df.groupby(YEAR, as_index=True).sum()
        df = df.sort_index(ascending=True, axis=0)

        return df

    def _compute_cumulated_documents(self, df):

        df[CUMUL_OCC] = df[OCC].cumsum()

        return df

    def _compute_citable_years(self, df):

        current_year = df.index.max()
        df[CITAB_YEAR] = current_year - df.index + 1

        return df

    def _compute_global_citation_metrics(self, df):

        df[MEAN_GCS] = df[GCS] / df[OCC]
        df[CUMUL_GCS] = df[GCS].cumsum()
        df[MEAN_GCS_PER_YEAR] = df[MEAN_GCS] / df[CITAB_YEAR]
        df[MEAN_GCS_PER_YEAR] = df[MEAN_GCS_PER_YEAR].round(2)

        return df

    def _compute_local_citation_metrics(self, df):

        df[MEAN_LCS] = df[LCS] / df[OCC]
        df[CUMUL_LCS] = df[LCS].cumsum()
        df[MEAN_LCS_PER_YEAR] = df[MEAN_LCS] / df[CITAB_YEAR]
        df[MEAN_LCS_PER_YEAR] = df[MEAN_LCS_PER_YEAR].round(2)

        return df

    def _reorder_columns(self, df):

        return df[
            [
                OCC,
                CUMUL_OCC,
                CITAB_YEAR,
                GCS,
                CUMUL_GCS,
                MEAN_GCS,
                MEAN_GCS_PER_YEAR,
                LCS,
                CUMUL_LCS,
                MEAN_LCS,
                MEAN_LCS_PER_YEAR,
            ]
        ]

    def run(self):

        df = load_filtered_main_csv_zip(params=self.params)

        df = self._select_columns(df)
        df = self._group_by_year_and_sort(df)
        df = self._compute_cumulated_documents(df)
        df = self._compute_citable_years(df)
        df = self._compute_global_citation_metrics(df)
        df = self._compute_local_citation_metrics(df)
        df = self._reorder_columns(df)

        return df
