# flake8: noqa
"""
.. _ranking_chart:

Ranking Chart
===============================================================================

Default visualization chart for Bibliometrix.


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/ranking_chart.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )
>>> chart = techminer2plus.ranking_chart(itemslist, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/ranking_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


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
class RankingChart:
    """Bar Chart.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame


# pylint: disable=too-many-arguments
def ranking_chart(
    itemslist=None,
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
):
    """Creates a rank chart."""

    metric_label = (
        itemslist.metric_.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        itemslist.field_.replace("_", " ").upper() + " RANKING"
        if field_label is None
        else field_label
    )

    table = itemslist.items_list_.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y=itemslist.metric_,
        hover_data=itemslist.items_list_.columns.to_list(),
        markers=True,
    )

    fig.update_traces(
        marker={
            "size": marker_size,
            "line": {"color": line_color, "width": 0},
        },
        marker_color=line_color,
        line={"color": line_color, "width": line_width},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=metric_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=field_label,
    )

    for name, row in table.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row[itemslist.metric_],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return RankingChart(
        plot_=fig,
        table_=itemslist.items_list_[itemslist.metric_],
    )
