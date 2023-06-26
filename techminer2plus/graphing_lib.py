"""Graphing library."""

from dataclasses import dataclass

import plotly.express as px
import plotly.graph_objs as go

from .list_items import ItemsList


def bar_chart(
    items_list,
    title=None,
    metric_label=None,
    field_label=None,
):
    """Bar chart."""

    if metric_label is None:
        metric_label = items_list.metric_.replace("_", " ").upper()

    fig = px.bar(
        items_list.table_,
        x=items_list.metric_,
        y=None,
        hover_data=items_list.table_.columns.to_list(),
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

    return fig


# pylint: disable=too-many-instance-attributes
