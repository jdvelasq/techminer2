"""
UnitsByYear
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.performance_metrics.trends import UnitsByYear
    >>> df = (
    ...     UnitsByYear()
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                           2015                   2016                   2017                           2018                         2019                          2020                      2021                 2022                     2023                     2024
    0               debit cards                fintech                fintech                        fintech                      fintech                       fintech                   fintech              fintech                  fintech                  fintech
    1       electronic commerce             innovation                finance                        finance                      finance          financial technology      financial technology              finance          economic growth  sustainable development
    2         financial service                finance    financial inclusion              financial service               sustainability                    blockchain             green finance                china            green finance                    china
    3          internet banking             technology             innovation             financial services      sustainable development            financial services                     china  financial inclusion               innovation            green economy
    4  research and application       content analysis   digital technologies                business models         perceived usefulness                 systemic risk         financial markets           innovation           sustainability         natural resource
    5         virtual addresses         digitalization               commerce                     blockchain      artificial intelligence           financial inclusion               industry 40             covid-19  sustainable development        natural resources
    6                 biometric          popular press  financial institution  financial services industries                       robots                sustainability                efficiency        green finance      financial inclusion           sustainability
    7      fast identity online               commerce  peer-to-peer networks                        surveys                        china  partial least square ( pls )                   banking   fintech innovation                  finance                  banking
    8                      fido                banking                  banks                 cyber security              decision making  structural equation modeling  environmental protection           panel data                    china                  finance
    9                  password  financial institution        digital finance            marketplace lending  design/methodology/approach              electronic money         green consumption              banking    financing constraints     financial technology

    >>> df = (
    ...     UnitsByYear()
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
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 0
    True
    >>> df.shape[1] > 0
    True
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                     2015                             2016                             2017                                     2018                                   2019                                    2020                                2021                           2022                               2023                               2024
    0               debit cards 001:00018                fintech 012:01094                fintech 011:02846                        fintech 012:04574                      fintech 007:02148                       fintech 013:03639                   fintech 017:04915              fintech 013:03141                  fintech 017:02357                  fintech 017:01434
    1       electronic commerce 001:00018             innovation 003:00685                finance 005:00633                        finance 005:02386                      finance 003:00912          financial technology 003:00765      financial technology 005:01186              finance 005:01423          economic growth 005:00793  sustainable development 005:00405
    2         financial service 001:00018                finance 003:00466    financial inclusion 003:00918              financial service 004:02150               sustainability 003:00489                    blockchain 003:00673             green finance 003:01186                china 005:01419            green finance 005:00748                    china 003:00281
    3          internet banking 001:00018             technology 002:00650             innovation 003:00320             financial services 004:00917      sustainable development 003:00489            financial services 003:00670                     china 003:00788  financial inclusion 004:01127               innovation 005:00731            green economy 003:00266
    4  research and application 001:00018       content analysis 002:00283   digital technologies 002:00838                business models 003:02943         perceived usefulness 002:00859                 systemic risk 002:00958         financial markets 002:00618           innovation 003:01024           sustainability 004:00619         natural resource 003:00254
    5         virtual addresses 001:00018         digitalization 002:00283               commerce 002:00322                     blockchain 002:01678      artificial intelligence 002:00804           financial inclusion 002:00838               industry 40 002:00617             covid-19 003:00941  sustainable development 004:00583        natural resources 003:00254
    6                 biometric 001:00001          popular press 002:00283  financial institution 002:00322  financial services industries 002:01611                       robots 002:00749                sustainability 002:00668                efficiency 002:00562        green finance 003:00910      financial inclusion 003:00442           sustainability 003:00245
    7      fast identity online 001:00001               commerce 002:00099  peer-to-peer networks 002:00322                        surveys 002:00699                        china 002:00317  partial least square ( pls ) 002:00560                   banking 002:00451   fintech innovation 003:00810                  finance 003:00427                  banking 003:00241
    8                      fido 001:00001                banking 001:00402                  banks 002:00260                 cyber security 002:00639              decision making 002:00274  structural equation modeling 002:00560  environmental protection 001:00517           panel data 002:00655                    china 003:00415                  finance 003:00231
    9                  password 001:00001  financial institution 001:00402        digital finance 001:01152            marketplace lending 002:00450  design/methodology/approach 001:00605              electronic money 002:00484         green consumption 001:00517              banking 002:00648    financing constraints 003:00384     financial technology 003:00209



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin, SortAxesMixin
from tm2p.enum import Field, UnitOrderBy

from .year_to_item import YearToItems

GCS = Field.GCS.value
OCC = UnitOrderBy.OCC.value
YEAR = Field.YEAR.value

COUNTERS = "COUNTERS"


class UnitsByYear(
    ParamsMixin,
    SortAxesMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        y2i = YearToItems().update(**self.params.__dict__).run()

        df = pd.DataFrame.from_dict(y2i, orient="index").T
        df = df.fillna("")
        df = df.sort_index(axis=1)

        return df
