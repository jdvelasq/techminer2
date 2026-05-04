"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.perform_metr.lotka import Metrics  # type: ignore
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
        N_DOCS  N_AUTH_OBS  PROP_AUTH_OBS  N_AUTH_THEO  PROP_AUTH_THEO  ABS_DIFF
    0        1        3523         0.8021    3523.0000          0.6270    0.1751
    1        2         524         0.1193     880.7500          0.1567    0.0374
    2        3         159         0.0362     391.4444          0.0697    0.0335
    3        4          66         0.0150     220.1875          0.0392    0.0242
    4        5          39         0.0089     140.9200          0.0251    0.0162
    5        6          20         0.0046      97.8611          0.0174    0.0128
    6        7          11         0.0025      71.8980          0.0128    0.0103
    7        8           9         0.0020      55.0469          0.0098    0.0078
    8        9           4         0.0009      43.4938          0.0077    0.0068
    9       10           9         0.0020      35.2300          0.0063    0.0043
    10      11           2         0.0005      29.1157          0.0052    0.0047
    11      12           6         0.0014      24.4653          0.0044    0.0030
    12      13           1         0.0002      20.8462          0.0037    0.0035
    13      14           4         0.0009      17.9745          0.0032    0.0023
    14      15           5         0.0011      15.6578          0.0028    0.0017
    15      16           4         0.0009      13.7617          0.0024    0.0015
    16      18           1         0.0002      10.8735          0.0019    0.0017
    17      20           1         0.0002       8.8075          0.0016    0.0014
    18      21           1         0.0002       7.9887          0.0014    0.0012
    19      27           1         0.0002       4.8326          0.0009    0.0007
    20      35           1         0.0002       2.8759          0.0005    0.0003
    21      41           1         0.0002       2.0958          0.0004    0.0002


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, UnitOrderBy
from tm2p.portfolio.perform_metr.unit import Metrics as AuthMetrics


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = self._compute_author_metrics()
        df = self._compute_observed_num_authors(df)
        df = self._compute_prop_of_observed_num_authors(df)
        df = self._compute_theoretical_num_authors(df)
        df = self._compute_prop_of_theoretical_num_authors(df)
        df = self._compute_abs_diff(df)

        return df

    def _compute_abs_diff(self, df):
        df["ABS_DIFF"] = (df["PROP_AUTH_OBS"] - df["PROP_AUTH_THEO"]).abs().round(4)
        return df

    def _compute_prop_of_theoretical_num_authors(self, df):
        total_theoretical_num_authors = df["N_AUTH_THEO"].sum()
        df["PROP_AUTH_THEO"] = (
            df["N_AUTH_THEO"].map(lambda x: x / total_theoretical_num_authors).round(4)
        )
        return df

    def _compute_theoretical_num_authors(self, df):
        total_authors = df["N_AUTH_OBS"].max()
        df["N_AUTH_THEO"] = (
            df["N_DOCS"].map(lambda x: total_authors / float(x * x)).round(4)
        )
        return df

    def _compute_prop_of_observed_num_authors(self, df):
        df["PROP_AUTH_OBS"] = (
            df["N_AUTH_OBS"].map(lambda x: x / df["N_AUTH_OBS"].sum()).round(4)
        )
        return df

    def _compute_observed_num_authors(self, df):
        df = df[["OCC"]]
        df = df.groupby(["OCC"], as_index=False).size()
        df.columns = ["N_DOCS", "N_AUTH_OBS"]
        df = df.sort_values(by="N_DOCS", ascending=True)
        df = df.reset_index(drop=True)
        df = df[["N_DOCS", "N_AUTH_OBS"]]
        return df

    def _compute_author_metrics(self):
        return (
            AuthMetrics()
            .update(**self.params.__dict__)
            #
            .with_analysis_unit(AnalysisUnit.AUTH)
            #
            .having_top_n_units(None)
            .having_unit_global_citation_between(None, None)
            .having_unit_occurrence_between(None, None)
            .having_units_in(None)
            .having_units_ordered_by(UnitOrderBy.OCC)
            #
            .run()
        )
