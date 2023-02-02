"""
RPYS (Reference Publication Year Spectroscopy)
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__rpys.html"

>>> from techminer2 import bibliometrix__rpys
>>> bibliometrix__rpys(directory=directory).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__rpys.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> bibliometrix__rpys(directory=directory).table_.head()
      Num References  Median
1937               1    -1.0
1938               0     0.0
1939               0     0.0
1940               0     0.0
1941               0     0.0


"""
import os.path
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def bibliometrix__rpys(
    directory="./",
    starting_year=None,
    ending_year=None,
):
    """Reference Publication Year Spectroscopy."""

    references = pd.read_csv(
        os.path.join(directory, "processed", "_references.csv"),
        sep=",",
        encoding="utf-8",
    )
    indicator = _compute_rpys(references)
    if starting_year is not None:
        indicator = indicator.loc[starting_year:]
    if ending_year is not None:
        indicator = indicator.loc[:ending_year]

    fig = _plot_rpys(indicator)

    result = _Results()
    result.table_ = indicator
    result.plot_ = fig
    return result


def _plot_rpys(indicator):

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=indicator.index,
            y=indicator["Num References"],
            fill="tozeroy",
            name="Num References",
            opacity=0.3,
            marker_color="lightgrey",  # darkslategray
        )
    )
    fig.add_trace(
        go.Scatter(
            x=indicator.index,
            y=indicator["Median"],
            fill="tozeroy",
            name="Median",
            opacity=0.8,
            marker_color="darkslategray",
        )
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title="Reference Spectroscopy",
    )

    fig.update_traces(
        marker=dict(
            size=6,
            line=dict(color="darkslategray", width=2),
        ),
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title="Cited References",
    )

    return fig


def _compute_rpys(references):

    references = references[["year"]]
    references = references.dropna()
    references_by_year = references["year"].value_counts()

    year_min = references_by_year.index.min()
    year_max = references_by_year.index.max()
    years = list(range(year_min, year_max + 1))

    indicator = pd.DataFrame(
        {
            "Num References": 0,
        },
        index=years,
    )

    indicator.loc[references_by_year.index, "Num References"] = references_by_year
    indicator = indicator.sort_index(axis=0, ascending=True)
    indicator["Median"] = (
        indicator["Num References"].rolling(window=5).median().fillna(0)
    )

    indicator["Median"] = indicator["Median"] - indicator["Num References"]
    return indicator
