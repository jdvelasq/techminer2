"""
ItemsByYear
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.performance_metrics.trends import ItemsByYear
    >>> df = (
    ...     ItemsByYear()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
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
                       2015                   2016                           2017                   2018                     2019                     2020                      2021                 2022                     2023                     2024
    0             biometric                fintech                        fintech                fintech                  fintech                  fintech                   fintech              fintech                  fintech                  fintech
    1  fast identity online             innovation            financial inclusion     financial services  artificial intelligence     financial technology      financial technology  financial inclusion            green finance        natural resources
    2                  fido             technology                     innovation        business models                   robots               blockchain             green finance        green finance      financial inclusion                  banking
    3              password       content analysis                          banks         cyber security                  finance            systemic risk                     china   fintech innovation    financing constraints   digital transformation
    4                   pki         digitalization                digital finance    marketplace lending            robo-advisors      financial inclusion  environmental protection                china          brics economies                    trust
    5        single sign-on          popular press                      e-finance         mobile payment      technology adoption           sustainability         green consumption             covid-19        carbon neutrality          economic growth
    6                                      banking  future research opportunities  disruptive innovation         entrepreneurship  artificial intelligence           cost efficiency              banking            co2 emissions   financial technologies
    7                        financial institution              literature review     financial startups   financial institutions                 covid-19              metafrontier    income inequality        energy innovation  sustainable development
    8                           financial services               state of the art         online banking                 startups                  banking     technology gap ratios  quantile regression          economic growth               blockchain
    9                                     research           behavioral economics           real options                 adoption         cryptocurrencies         access to finance         green credit  sustainable development      financial inclusion


    >>> df = (
    ...     ItemsByYear()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
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
                                 2015                             2016                                     2017                             2018                               2019                               2020                                2021                           2022                               2023                               2024
    0             biometric 001:00001                fintech 011:01029                        fintech 011:02846                fintech 012:04574                  fintech 006:01543                  fintech 013:03639                   fintech 017:04915              fintech 013:03141                  fintech 017:02357                  fintech 017:01434
    1  fast identity online 001:00001             innovation 003:00685            financial inclusion 003:00918     financial services 004:00917  artificial intelligence 002:00804     financial technology 003:00765      financial technology 005:01186  financial inclusion 004:01127            green finance 005:00748        natural resources 003:00254
    2                  fido 001:00001             technology 002:00650                     innovation 002:00273        business models 002:01516                   robots 002:00749               blockchain 003:00673             green finance 003:01186        green finance 003:00910      financial inclusion 003:00442                  banking 003:00241
    3              password 001:00001       content analysis 002:00283                          banks 002:00260         cyber security 002:00639                  finance 001:00605            systemic risk 002:00958                     china 002:00608   fintech innovation 003:00810    financing constraints 003:00384   digital transformation 002:00197
    4                   pki 001:00001         digitalization 002:00283                digital finance 001:01152    marketplace lending 002:00450            robo-advisors 001:00605      financial inclusion 002:00838  environmental protection 001:00517                china 003:00749          brics economies 002:00371                    trust 002:00178
    5        single sign-on 001:00001          popular press 002:00283                      e-finance 001:01152         mobile payment 002:00273      technology adoption 001:00605           sustainability 002:00668         green consumption 001:00517             covid-19 002:00686        carbon neutrality 002:00371          economic growth 002:00169
    6                                                banking 001:00402  future research opportunities 001:01152  disruptive innovation 001:01080         entrepreneurship 001:00530  artificial intelligence 002:00463           cost efficiency 001:00401              banking 002:00648            co2 emissions 002:00371   financial technologies 002:00144
    7                                  financial institution 001:00402              literature review 001:01152     financial startups 001:01080   financial institutions 001:00530                 covid-19 002:00330              metafrontier 001:00401    income inequality 001:00528        energy innovation 002:00371  sustainable development 002:00139
    8                                     financial services 001:00402               state of the art 001:01152         online banking 001:01080                 startups 001:00530                  banking 001:00770     technology gap ratios 001:00401  quantile regression 001:00528          economic growth 002:00306               blockchain 002:00137
    9                                               research 001:00402           behavioral economics 001:00563           real options 001:01080                 adoption 001:00425         cryptocurrencies 001:00770         access to finance 001:00393         green credit 001:00507  sustainable development 002:00280      financial inclusion 002:00137

"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin, SortAxesMixin
from tm2p.enum import Field, UnitOrderBy

from .year_to_items import YearToItems

GCS = Field.GCS.value
OCC = UnitOrderBy.OCC.value
YEAR = Field.YEAR.value

COUNTERS = "COUNTERS"


class ItemsByYear(
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
