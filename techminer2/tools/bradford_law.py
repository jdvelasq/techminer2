# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bradford's Law
===============================================================================

>>> from techminer2.analyze.contributors.sources import bradford_law
>>> bradford = bradford_law(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(bradford.df_.to_markdown())
|    |   Num Sources | %       |   Acum Num Sources | % Acum   |   Documents published |   Tot Documents published |   Num Documents | Tot Documents   |   Bradford's Group |
|---:|--------------:|:--------|-------------------:|:---------|----------------------:|--------------------------:|----------------:|:----------------|-------------------:|
|  0 |             1 | 2.44 %  |                  1 | 2.44 %   |                     3 |                         3 |               3 | 6.0 %           |                  1 |
|  1 |             7 | 17.07 % |                  8 | 19.51 %  |                     2 |                        14 |              17 | 34.0 %          |                  2 |
|  2 |            33 | 80.49 % |                 41 | 100.0 %  |                     1 |                        33 |              50 | 100.0 %         |                  3 |

    

>>> print(bradford.zones_.to_markdown())
| abbr_source_title                   |   no |   OCC |   cum_OCC |   global_citations |   zone |
|:------------------------------------|-----:|------:|----------:|-------------------:|-------:|
| J. Econ. Bus.                       |    1 |     3 |         3 |                422 |      1 |
| J Manage Inf Syst                   |    2 |     2 |         5 |                696 |      1 |
| Rev. Financ. Stud.                  |    3 |     2 |         7 |                432 |      1 |
| Ind Manage Data Sys                 |    4 |     2 |         9 |                386 |      1 |
| Electron. Mark.                     |    5 |     2 |        11 |                287 |      1 |
| Financial Innov.                    |    6 |     2 |        13 |                190 |      1 |
| Financ. Manage.                     |    7 |     2 |        15 |                161 |      1 |
| Sustainability                      |    8 |     2 |        17 |                150 |      2 |
| Bus. Horiz.                         |    9 |     1 |        18 |                557 |      2 |
| J. Bus. Econ.                       |   10 |     1 |        19 |                489 |      2 |
| J. Financ. Econ.                    |   11 |     1 |        20 |                390 |      2 |
| New Polit. Econ.                    |   12 |     1 |        21 |                314 |      2 |
| Small Bus. Econ.                    |   13 |     1 |        22 |                258 |      2 |
| Busin. Info. Sys. Eng.              |   14 |     1 |        23 |                253 |      2 |
| J Network Comput Appl               |   15 |     1 |        24 |                238 |      2 |
| J. Innov. Manag.                    |   16 |     1 |        25 |                226 |      2 |
| Int J Inf Manage                    |   17 |     1 |        26 |                180 |      2 |
| Northwest. J. Intl. Law Bus.        |   18 |     1 |        27 |                178 |      2 |
| Symmetry                            |   19 |     1 |        28 |                176 |      2 |
| J Strategic Inform Syst             |   20 |     1 |        29 |                160 |      2 |
| Telecommun Policy                   |   21 |     1 |        30 |                146 |      2 |
| Account. Financ.                    |   22 |     1 |        31 |                145 |      2 |
| Int. J. Appl. Eng. Res.             |   23 |     1 |        32 |                125 |      2 |
| Int. J. Hum.-Comput. Interact.      |   24 |     1 |        33 |                121 |      3 |
| Inf. Comput. Security               |   25 |     1 |        34 |                104 |      3 |
| Elect. Commer. Res. Appl.           |   26 |     1 |        35 |                102 |      3 |
| Risk Manage.                        |   27 |     1 |        36 |                102 |      3 |
| J.  Financ. Regul.                  |   28 |     1 |        37 |                101 |      3 |
| FinTech in Ger.                     |   29 |     1 |        38 |                100 |      3 |
| China Econ. J.                      |   30 |     1 |        39 |                 96 |      3 |
| Contemp. Stud. Econ. Financ. Anal.  |   31 |     1 |        40 |                 96 |      3 |
| Energy Procedia                     |   32 |     1 |        41 |                 90 |      3 |
| Lect. Notes Comput. Sci.            |   33 |     1 |        42 |                 85 |      3 |
| Hum.-centric Comput. Inf. Sci.      |   34 |     1 |        43 |                 82 |      3 |
| Vanderbilt Law Rev.                 |   35 |     1 |        44 |                 81 |      3 |
| London Bus. Sch. Rev.               |   36 |     1 |        45 |                 76 |      3 |
| Int. Conf. Inf. Syst., ICIS         |   37 |     1 |        46 |                 75 |      3 |
| Eur. Res. Stud.                     |   38 |     1 |        47 |                 67 |      3 |
| Georget. Law J.                     |   39 |     1 |        48 |                 67 |      3 |
| Curr. Opin. Environ. Sustainability |   40 |     1 |        49 |                 66 |      3 |
| Foresight                           |   41 |     1 |        50 |                 65 |      3 |


>>> bradford.fig_.write_html("sphinx/_static/analyze/contributors/sources/bradford_law.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/sources/bradford_law.html")
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px

from ..read_records import read_records


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

    indicators = records[["abbr_source_title", "global_citations"]]
    indicators = indicators.assign(OCC=1)
    indicators = indicators.groupby(["abbr_source_title"], as_index=False).sum()
    indicators = indicators.sort_values(by=["OCC", "global_citations"], ascending=False)
    indicators = indicators.assign(cum_OCC=indicators["OCC"].cumsum())
    indicators = indicators.assign(no=1)
    indicators = indicators.assign(no=indicators.no.cumsum())

    cum_occ = indicators["OCC"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(
        indicators.cum_OCC >= int(cum_occ * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(indicators.cum_OCC >= int(cum_occ / 3), 1)
    indicators = indicators.set_index("abbr_source_title")
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

    sources["Tot Documents published"] = (
        sources["Num Sources"] * sources["Documents published"]
    )
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
