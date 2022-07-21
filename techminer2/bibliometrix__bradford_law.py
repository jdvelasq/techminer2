"""
Bradford's Law
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__bradford_law.html"

>>> from techminer2 import bibliometrix__bradford_law
>>> bibliometrix__bradford_law(
...     directory=directory,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__bradford_law.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> bibliometrix__bradford_law(
...     directory=directory,
... ).source_clustering_.head(5)
                     no  OCC  cum_OCC  global_citations  zone
source_abbr                                                  
CEUR WORKSHOP PROC    1    5        5                 2     1
STUD COMPUT INTELL    2    4        9                 3     1
JUSLETTER IT          3    4       13                 0     1
EUR BUS ORG LAW REV   4    3       16                65     1
J BANK REGUL          5    3       19                29     1


>>> bibliometrix__bradford_law(
...     directory=directory,
... ).core_sources_.head(5)
   Num Sources        %  ...  Tot Documents Bradford's Group
0            1   1.49 %  ...         5.32 %                1
1            2   2.99 %  ...        13.83 %                1
2            4   5.97 %  ...         26.6 %                1
3            9  13.43 %  ...        45.74 %                2
4           51  76.12 %  ...        100.0 %                3
<BLANKLINE>
[5 rows x 9 columns]


"""
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px

from ._read_records import read_records
from .explode import explode


@dataclass(init=False)
class _Result:
    plot_: None
    source_clustering_: None
    core_sources_: None


def bibliometrix__bradford_law(
    directory="./",
    database="documents",
):
    """Bradfor's Law"""

    results = _Result()

    results.source_clustering_ = _source_clustering(
        directory=directory,
        database=database,
    )

    results.plot_ = _bradford_law_plot(
        indicators=results.source_clustering_,
    )

    results.core_sources_ = _core_sources(directory=directory)

    return results


def _core_sources(directory):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """
    documents = read_records(
        directory=directory, database="documents", use_filter=False
    )

    documents["num_documents"] = 1
    documents = explode(
        documents[
            [
                "source_title",
                "num_documents",
                "article",
            ]
        ],
        "source_title",
        sep="; ",
    )

    sources = documents.groupby("source_title", as_index=True).agg(
        {
            "num_documents": np.sum,
        }
    )
    sources = sources[["num_documents"]]
    sources = sources.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(sources), 2)) + " %" for a in sources]
    sources = pd.DataFrame(
        {"Num Sources": sources.tolist(), "%": w, "Documents published": sources.index}
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

    bradford1 = int(len(documents) / 3)
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


def _source_clustering(
    directory="./",
    database="documents",
):
    """Source clustering throught Bradfors's Law."""

    records = read_records(directory=directory, database=database, use_filter=False)

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
    indicators.zone = indicators.zone.where(
        indicators.cum_OCC >= int(cum_occ * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(indicators.cum_OCC >= int(cum_occ / 3), 1)
    indicators = indicators.set_index("source_abbr")
    indicators = indicators[["no", "OCC", "cum_OCC", "global_citations", "zone"]]

    return indicators


def _bradford_law_plot(
    indicators,
):

    fig = px.line(
        indicators,
        x="no",
        y="OCC",
        title="Source Clustering through Bradford's Law",
        markers=True,
        hover_data=[indicators.index, "OCC"],
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

    core = len(indicators.loc[indicators.zone == 1])

    fig.add_shape(
        type="rect",
        x0=1,
        y0=0,
        x1=core,
        y1=indicators.OCC.max(),
        line=dict(
            color="lightgrey",
            width=2,
        ),
        fillcolor="lightgrey",
        opacity=0.2,
    )

    fig.data = fig.data[::-1]

    return fig
