# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _global_indicators_by_year_chart:

Global Indicators by Year chart
===============================================================================

Creates a time line chart from an indicator from  :ref:`global_indicators_by_year`.



>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/global_indicators_by_year_chart.html"
>>> tm2.global_indicators_by_year_chart(
...     root_dir=root_dir,
...     indicator_to_plot="mean_global_citations",
...     title="Average Citations per Year",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/global_indicators_by_year_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .global_metrics_by_year_table import global_metrics_by_year_table


def global_metrics_by_year_chart(
    indicator_to_plot: str,
    title: str,
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Makes a time line plot for indicators."""

    df = global_metrics_by_year_table(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    column_names = {
        column: column.replace("_", " ").title()
        for column in df.columns
        if column not in ["OCC", "cum_OCC"]
    }
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum_OCC"
    df = df.rename(columns=column_names)

    fig = px.line(
        df,
        x=df.index,
        y=column_names[indicator_to_plot],
        title=title,
        markers=True,
        hover_data=["OCC", "Global Citations", "Local Citations"],
    )
    fig.update_traces(
        marker={"size": 10, "line": dict(color="#556f81", width=2)},
        marker_color="#8da4b4",
        line={"color": "#556f81"},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
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
    return fig
