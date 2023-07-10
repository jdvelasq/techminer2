# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _bradford_law:

Bradford's Law
===============================================================================



>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> print(tm2p.bradford_law_sources_by_zone(
...     root_dir=root_dir,
... ).to_markdown())
| source_abbr                   |   no |   OCC |   cum_OCC |   global_citations |   zone |
|:------------------------------|-----:|------:|----------:|-------------------:|-------:|
| J BANK REGUL                  |    1 |     2 |         2 |                 35 |      1 |
| J FINANC CRIME                |    2 |     2 |         4 |                 13 |      1 |
| FOSTER INNOVCOMPET WITH FINTE |    3 |     2 |         6 |                  1 |      1 |
| STUD COMPUT INTELL            |    4 |     2 |         8 |                  1 |      1 |
| INT CONF INF TECHNOL SYST INN |    5 |     2 |        10 |                  0 |      1 |
| ROUTLEDGE HANDBFINANCIAL TECH |    6 |     2 |        12 |                  0 |      1 |
| J ECON BUS                    |    7 |     1 |        13 |                153 |      1 |
| NORTHWEST J INTL LAW BUS      |    8 |     1 |        14 |                150 |      1 |
| PALGRAVE STUD DIGIT BUS ENABL |    9 |     1 |        15 |                 33 |      1 |
| DUKE LAW J                    |   10 |     1 |        16 |                 30 |      1 |
| J RISK FINANC                 |   11 |     1 |        17 |                 21 |      2 |
| J MONEY LAUND CONTROL         |   12 |     1 |        18 |                 14 |      2 |
| FINANCIAL INNOV               |   13 |     1 |        19 |                 13 |      2 |
| ICEIS - PROC INT CONF ENTERP  |   14 |     1 |        20 |                 12 |      2 |
| HANDBBLOCKCHAIN, DIGIT FINANC |   15 |     1 |        21 |                 11 |      2 |
| HELIYON                       |   16 |     1 |        22 |                 11 |      2 |
| J RISK MANG FINANCIAL INST    |   17 |     1 |        23 |                  8 |      2 |
| ADV INTELL SYS COMPUT         |   18 |     1 |        24 |                  7 |      2 |
| ADELAIDE LAW REV              |   19 |     1 |        25 |                  5 |      2 |
| INTELL SYST ACCOUNT FINANCE M |   20 |     1 |        26 |                  5 |      2 |
| J FINANCIAL DATA SCI          |   21 |     1 |        27 |                  5 |      2 |
| LECTURE NOTES DATA ENG COMMUN |   22 |     1 |        28 |                  4 |      2 |
| UNIV NEW SOUTH WALES LAW J    |   23 |     1 |        29 |                  4 |      2 |
| EUR J RISK REGUL              |   24 |     1 |        30 |                  3 |      2 |
| FRONTIER ARTIF INTELL         |   25 |     1 |        31 |                  3 |      2 |
| J ADV RES DYN CONTROL SYST    |   26 |     1 |        32 |                  3 |      2 |
| J ANTITRUST ENFORC            |   27 |     1 |        33 |                  3 |      2 |
| PROC - IEEE WORLD CONGR SERV, |   28 |     1 |        34 |                  3 |      3 |
| ACM INT CONF PROC SER         |   29 |     1 |        35 |                  2 |      3 |
| CEUR WORKSHOP PROC            |   30 |     1 |        36 |                  2 |      3 |
| LECT NOTES BUS INF PROCESS    |   31 |     1 |        37 |                  2 |      3 |
| DECIS SUPPORT SYST            |   32 |     1 |        38 |                  1 |      3 |
| EAI/SPRINGER INNO COMM COMP   |   33 |     1 |        39 |                  1 |      3 |
| J IND BUS ECON                |   34 |     1 |        40 |                  1 |      3 |
| LECT NOTES NETWORKS SYST      |   35 |     1 |        41 |                  1 |      3 |
| PROC EUR CONF INNOV ENTREPREN |   36 |     1 |        42 |                  1 |      3 |
| PROC INT CONF ELECTRON BUS (I |   37 |     1 |        43 |                  1 |      3 |
| COMPUTER                      |   38 |     1 |        44 |                  0 |      3 |
| EUR BUS LAW REV               |   39 |     1 |        45 |                  0 |      3 |
| FINTECH: LAWREGULATION        |   40 |     1 |        46 |                  0 |      3 |
| J CORP FINANC                 |   41 |     1 |        47 |                  0 |      3 |
| J FINANC REGUL COMPLIANCE     |   42 |     1 |        48 |                  0 |      3 |
| JUSLETTER IT                  |   43 |     1 |        49 |                  0 |      3 |
| NEW POLIT ECON                |   44 |     1 |        50 |                  0 |      3 |
| RES INT BUS FINANC            |   45 |     1 |        51 |                  0 |      3 |
| TECHNOL SOC                   |   46 |     1 |        52 |                  0 |      3 |


"""
from ._read_records import read_records


def bradford_law_sources_by_zone(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Source clustering throught Bradfors's Law."""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = records[["source_abbr", "global_citations"]]
    indicators = indicators.assign(OCC=1)
    indicators = indicators.groupby(["source_abbr"], as_index=False).sum()
    indicators = indicators.sort_values(
        by=["OCC", "global_citations"], ascending=False
    )
    indicators = indicators.assign(cum_OCC=indicators["OCC"].cumsum())
    indicators = indicators.assign(no=1)
    indicators = indicators.assign(no=indicators.no.cumsum())

    cum_occ = indicators["OCC"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(
        indicators.cum_OCC >= int(cum_occ * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(
        indicators.cum_OCC >= int(cum_occ / 3), 1
    )
    indicators = indicators.set_index("source_abbr")
    indicators = indicators[
        ["no", "OCC", "cum_OCC", "global_citations", "zone"]
    ]

    return indicators
