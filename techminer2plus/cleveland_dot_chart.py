# flake8: noqa
"""
.. _cleveland_dot_chart:

Cleveland Dot Chart
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/cleveland_chart.html"


>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )

>>> chart = techminer2plus.cleveland_dot_chart(itemslist, title="Most Frequent Author Keywords")
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/cleveland_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

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
class ClevelandDotChart:
    """Bar Chart.

    :meta private:
    """

    fig_: go.Figure
    df_: pd.DataFrame


def cleveland_dot_chart(
    data=None,
    title=None,
    metric_label=None,
    field_label=None,
):
    """Creates a cleveland doc chart.

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

    fig = px.scatter(
        data.df_,
        x=data.metric_,
        y=None,
        hover_data=data.df_.columns.to_list(),
        size=data.metric_,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker=dict(
            size=12,
            line=dict(color="black", width=2),
        ),
        marker_color="slategray",
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
        gridcolor="gray",
        griddash="solid",
        title_text=field_label,
    )

    return ClevelandDotChart(
        fig_=fig,
        df_=data.df_[data.metric_],
    )
