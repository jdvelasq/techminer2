# flake8: noqa
"""
.. _line_chart:

Line Chart
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/line_chart.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...     field='author_keywords',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> chart = techminer2plus.line_chart(itemslist, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/line_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.table_.head()
author_keywords
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
COMPLIANCE                7
REGULATION                5
Name: OCC, dtype: int64



# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


@dataclass
class LineChart:
    """Bar Chart.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame


def line_chart(
    itemslist=None,
    title=None,
    field_label=None,
    metric_label=None,
):
    """Creates a line chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.

    Returns:
        BasicChart: A basic chart object.

    """
    metric_label = (
        itemslist.metric_.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        itemslist.field_.replace("_", " ").upper()
        if field_label is None
        else field_label
    )

    fig = px.line(
        itemslist.items_list_,
        x=None,
        y=itemslist.metric_,
        hover_data=itemslist.items_list_.columns.to_list(),
        markers=True,
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title,
    )
    fig.update_traces(
        marker=dict(size=9, line=dict(color="darkslategray", width=2)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        title_text=field_label,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=metric_label,
    )

    return LineChart(
        plot_=fig,
        table_=itemslist.items_list_[itemslist.metric_],
    )
