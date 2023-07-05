# flake8: noqa
# pylint: disable=line-too-long
"""
RPYS (Reference Publication Year Spectroscopy)
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/cited_references/rpys.html"

>>> import techminer2plus
>>> techminer2plus.publish.cited_references.rpys(root_dir=root_dir).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/cited_references/rpys.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> techminer2plus.publish.cited_references.rpys(root_dir=root_dir).table_.head()
      Num References  Median
1937               1    -1.0
1938               0     0.0
1939               0     0.0
1940               0     0.0
1941               0     0.0

"""
import os.path

import pandas as pd
import plotly.graph_objects as go

# from ...classes import BasicChart
# from ...records_lib import read_records


def rpys(
    # Database options:
    root_dir="./",
    database="references",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Reference Publication Year Spectroscopy."""

    references = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicator = _compute_rpys(references)
    if year_filter is not None:
        indicator = indicator.loc[year_filter:]
    if cited_by_filter is not None:
        indicator = indicator.loc[:cited_by_filter]

    fig = _plot_rpys(indicator)

    result = BasicChart()
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

    indicator.loc[
        references_by_year.index, "Num References"
    ] = references_by_year
    indicator = indicator.sort_index(axis=0, ascending=True)
    indicator["Median"] = (
        indicator["Num References"].rolling(window=5).median().fillna(0)
    )

    indicator["Median"] = indicator["Median"] - indicator["Num References"]
    return indicator
