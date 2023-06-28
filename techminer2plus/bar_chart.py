# flake8: noqa
"""
.. _bar_chart:

Bar Chart
===============================================================================

Displays a horizontal bar graph of the selected items in a ItemLlist object. 
Items in your list are the Y-axis, and the number of records are the X-axis.



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bar_chart.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...     field='author_keywords',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> chart = techminer2plus.bar_chart(itemslist, title="Most Frequent Author Keywords")
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
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
class BarChart:
    """Bar Chart.

    :meta private:
    """

    fig_: go.Figure
    df_: pd.DataFrame


def bar_chart(
    data=None,
    #
    # Chart params:
    title=None,
    metric_label=None,
    field_label=None,
):
    """Bar chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.

    Returns:
        BasicChart: A basic chart object.

    """
    metric_label = (
        data.metric_.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        data.field_.replace("_", " ").upper()
        if field_label is None
        else field_label
    )

    fig = px.bar(
        data.df_,
        x=data.metric_,
        y=None,
        hover_data=data.df_.columns.to_list(),
        orientation="h",
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker_color="rgb(171,171,171)",
        marker_line={"color": "darkslategray"},
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=metric_label,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        title_text=field_label,
    )

    return BarChart(
        fig_=fig,
        df_=data.df_[data.metric_],
    )
