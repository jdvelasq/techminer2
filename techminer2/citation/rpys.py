# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
.. _citation_analysis.rpys:

RPYS (Reference Publication Year Spectroscopy)
===============================================================================


>>> from techminer2.citation_analysis import rpys
>>> chart = rpys(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
... )
>>> chart.fig_.write_html("sphinx/_static/citation_analysis/rpys_chart.html")

.. raw:: html

    <iframe src="../../../../_static/citation_analysis/rpys_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
      Num References  Median
1937               1    -1.0
1938               0     0.0
1939               0     0.0
1940               0     0.0
1941               0     0.0


"""

from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from .._read_records import read_records


def rpys(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Reference Publication Year Spectroscopy.

    :meta private:
    """

    data_frame = __table(root_dir=root_dir)
    fig = __fig(data_frame)

    @dataclass
    class Results:
        df_ = data_frame
        fig_ = fig

    return Results()


def __table(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Reference Publication Year Spectroscopy."""

    references = read_records(
        root_dir=root_dir,
        database="references",
        year_filter=(None, None),
        cited_by_filter=(None, None),
    )

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
    indicator["Median"] = indicator["Num References"].rolling(window=5).median().fillna(0)

    indicator["Median"] = indicator["Median"] - indicator["Num References"]
    return indicator


def __fig(data_frame):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data_frame.index,
            y=data_frame["Num References"],
            fill="tozeroy",
            name="Num References",
            opacity=0.3,
            marker_color="lightgrey",  # darkslategray
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data_frame.index,
            y=data_frame["Median"],
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