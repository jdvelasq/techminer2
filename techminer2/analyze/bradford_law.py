# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bradford's Law
===============================================================================

>>> from techminer2.analyze import bradford_law
>>> bradford = bradford_law(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(bradford.df_.to_markdown())
|    |   Num Sources | %       |   Acum Num Sources | % Acum   |   Documents published |   Tot Documents published |   Num Documents | Tot Documents   |   Bradford's Group |
|---:|--------------:|:--------|-------------------:|:---------|----------------------:|--------------------------:|----------------:|:----------------|-------------------:|
|  0 |             6 | 13.04 % |                  6 | 13.04 %  |                     2 |                        12 |              12 | 23.08 %         |                  1 |
|  1 |            40 | 86.96 % |                 46 | 100.0 %  |                     1 |                        40 |              52 | 100.0 %         |                  3 |



>>> print(bradford.zones_.to_markdown())
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

>>> bradford.fig_.write_html("sphinx/_static/analyze/bradford_law_chart.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/bradford_law_chart.html")
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px

from .._read_records import read_records


def bradford_law(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Bradford's Law

    :meta private:
    """
    data_frame = __table(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    zones = __zones(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = __chart(zones)

    @dataclass
    class Results:
        df_ = data_frame
        fig_ = fig
        zones_ = zones

    return Results()


def __zones(
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
    indicators = indicators.sort_values(by=["OCC", "global_citations"], ascending=False)
    indicators = indicators.assign(cum_OCC=indicators["OCC"].cumsum())
    indicators = indicators.assign(no=1)
    indicators = indicators.assign(no=indicators.no.cumsum())

    cum_occ = indicators["OCC"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(indicators.cum_OCC >= int(cum_occ * 2 / 3), 2)
    indicators.zone = indicators.zone.where(indicators.cum_OCC >= int(cum_occ / 3), 1)
    indicators = indicators.set_index("source_abbr")
    indicators = indicators[["no", "OCC", "cum_OCC", "global_citations", "zone"]]

    return indicators


def __table(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records["num_documents"] = 1

    sources = records.groupby("source_title", as_index=True).agg(
        {
            "num_documents": np.sum,
        }
    )
    sources = sources[["num_documents"]]
    sources = sources.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(sources), 2)) + " %" for a in sources]
    sources = pd.DataFrame(
        {
            "Num Sources": sources.tolist(),
            "%": w,
            "Documents published": sources.index,
        }
    )

    sources = sources.sort_values(["Documents published"], ascending=False)
    sources["Acum Num Sources"] = sources["Num Sources"].cumsum()
    sources["% Acum"] = [
        str(round(100 * a / sum(sources["Num Sources"]), 2)) + " %"
        for a in sources["Acum Num Sources"]
    ]

    sources["Tot Documents published"] = sources["Num Sources"] * sources["Documents published"]
    sources["Num Documents"] = sources["Tot Documents published"].cumsum()
    sources["Tot Documents"] = sources["Num Documents"].map(
        lambda w: str(round(w / sources["Num Documents"].max() * 100, 2)) + " %"
    )

    bradford1 = int(len(records) / 3)
    bradford2 = 2 * bradford1

    sources["Bradford's Group"] = sources["Num Documents"].map(
        lambda w: 3 if w > bradford2 else (2 if w > bradford1 else 1)
    )

    sources = sources[
        [
            "Num Sources",
            "%",
            "Acum Num Sources",
            "% Acum",
            "Documents published",
            "Tot Documents published",
            "Num Documents",
            "Tot Documents",
            "Bradford's Group",
        ]
    ]

    sources = sources.reset_index(drop=True)

    return sources


def __chart(
    zones,
):
    """Bradfor's Law"""

    fig = px.line(
        zones,
        x="no",
        y="OCC",
        title="Source Clustering through Bradford's Law",
        markers=True,
        hover_data=[zones.index, "OCC"],
        log_x=True,
    )
    fig.update_traces(
        marker=dict(size=5, line=dict(color="darkslategray", width=1)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title=None,
        xaxis_showticklabels=False,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )

    core = len(zones.loc[zones.zone == 1])

    fig.add_shape(
        type="rect",
        x0=1,
        y0=0,
        x1=core,
        y1=zones.OCC.max(),
        line=dict(
            color="lightgrey",
            width=2,
        ),
        fillcolor="lightgrey",
        opacity=0.2,
    )

    fig.data = fig.data[::-1]

    return fig
