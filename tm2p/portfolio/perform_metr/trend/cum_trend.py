"""
CumulativeTrends
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.perform_metr.trends import CumulativeTrends
    >>> df = (
    ...     CumulativeTrends()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
    YEAR                     2015  2016  2017  2018  ...  2021  2022  2023  2024
    KW_NORM                                          ...
    fintech                     0    12    23    35  ...    72    85   102   119
    finance                     0     3     8    13  ...    18    23    26    29
    innovation                  0     3     6     7  ...    11    14    19    20
    china                       0     1     1     1  ...     7    12    15    18
    financial inclusion         0     1     4     5  ...     8    12    15    17
    financial technology        0     1     2     3  ...    12    12    13    16
    sustainable development     0     1     1     1  ...     5     6    10    15
    banking                     0     1     2     2  ...     6     8    10    13
    sustainability              0     0     0     0  ...     6     6    10    13
    blockchain                  0     1     2     4  ...     9     9    10    12
    <BLANKLINE>
    [10 rows x 10 columns]


    >>> df = (
    ...     CumulativeTrends()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> df.head(10)  # doctest: +NORMALIZE_WHITESPACE
    YEAR                               2015  2016  2017  ...  2022  2023  2024
    KW_NORM                                              ...
    fintech 119:26148                     0    12    23  ...    85   102   119
    finance 029:07137                     0     3     8  ...    23    26    29
    innovation 020:03916                  0     3     6  ...    14    19    20
    china 018:03596                       0     1     1  ...    12    15    18
    financial inclusion 017:03823         0     1     4  ...    12    15    17
    financial technology 016:02809        0     1     2  ...    12    13    16
    sustainable development 015:02158     0     1     1  ...     6    10    15
    banking 013:03043                     0     1     2  ...     8    10    13
    sustainability 013:02308              0     0     0  ...     6    10    13
    blockchain 012:03450                  0     1     2  ...     9    10    12
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from tm2p._intern import ParamsMixin

from .trend import Trends


class CumulativeTrends(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = Trends().update(**self.params.__dict__).run()
        df = df.cumsum(axis=1)
        return df
