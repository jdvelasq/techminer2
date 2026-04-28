"""
ZoneTable
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.perform_metr.bradford import ZoneTable
    >>> df = (
    ...     ZoneTable()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(20).to_string()) # doctest: +NORMALIZE_WHITESPACE
                                                                         RANK  N_DOCS  CUM_N_DOCS   GCS  ZONE
    SRC_ISO4
    SENSORS                                                                 1      42          42  1013     1
    IEEE ACCESS                                                             2      40          82   902     1
    IEEE INTERNET THINGS J                                                  3      31         113   670     1
    ACM INT CONF PROC SER                                                   4      28         141   250     1
    LECT NOTES NETWORKS SYST                                                5      25         166   100     1
    LECT NOTES ELECTR ENG                                                   6      21         187    94     1
    COMMUN COMPUT INFO SCI                                                  7      20         207    53     1
    ELECTRON (SWITZERLAND)                                                  8      17         224   221     1
    PROC INT JT CONF NEURAL NETWORKS                                        9      16         240   207     1
    INTERNET THING                                                         10      15         255   700     1
    IEEE SENSORS J                                                         11      15         270   401     1
    ACM TRANS EMBED COMPUT SYST                                            12      15         285   136     1
    TINYML EDGE INTELL IOT LPWAN NETWORKS                                  13      15         300    83     1
    SCI REP                                                                14      14         314   156     1
    IEEE TRANS CONSUM ELECTRON                                             15      13         327   163     1
    PROC IEEE INT SYMP CIRCUITS SYST                                       16      13         340   146     1
    IEEE INT CONF PERVASIVE COMPUT COMMUN WORK AFFIL EVENTS PERCOM WORK    17      13         353   118     1
    IEEE SENSORS APPL SYMP SAS - PROC                                      18      12         365   106     1
    LECT NOTES COMPUT SCI                                                  19      12         377    27     1
    INTERNET TECHNOL LETT                                                  20      12         389    10     1

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field

SRC_ISO4 = Field.SRC_ISO4.value
GCS = Field.GCS.value
N_DOCS = "N_DOCS"
CUM_N_DOCS = "CUM_N_DOCS"
ZONE = "ZONE"


class ZoneTable(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        records = load_filtered_main_csv_zip(params=self.params)

        indicators = records[[SRC_ISO4, GCS]]
        indicators = indicators.assign(N_DOCS=1)
        indicators = indicators.groupby([SRC_ISO4], as_index=False).sum()
        indicators = indicators.sort_values(by=[N_DOCS, GCS], ascending=False)
        indicators = indicators.assign(CUM_N_DOCS=indicators[N_DOCS].cumsum())
        indicators = indicators.assign(RANK=1)
        indicators = indicators.assign(RANK=indicators.RANK.cumsum())

        cum_occ = indicators[N_DOCS].sum()
        indicators = indicators.reset_index(drop=True)
        indicators = indicators.assign(ZONE=3)
        indicators.ZONE = indicators.ZONE.where(
            indicators.CUM_N_DOCS >= int(cum_occ * 2 / 3), 2
        )
        indicators.ZONE = indicators.ZONE.where(
            indicators.CUM_N_DOCS >= int(cum_occ / 3), 1
        )
        indicators = indicators.set_index(SRC_ISO4)
        indicators = indicators[["RANK", N_DOCS, CUM_N_DOCS, GCS, ZONE]]

        return indicators
