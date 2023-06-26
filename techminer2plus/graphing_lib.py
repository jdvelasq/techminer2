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
@dataclass
class RankingChart(ItemsList):
    """Ranking chart."""

    ranking_chart_: go.Figure

    def __init__(self, itemslist: ItemsList, fig):
        super().__init__(
            items_list_=itemslist.items_list_,
            chatbot_prompt_=itemslist.chatbot_prompt_,
            #
            # Params:
            field_=itemslist.field_,
            metric_=itemslist.metric_,
            #
            # Item filters:
            top_n_=itemslist.top_n_,
            occ_range_=itemslist.occ_range_,
            gc_range_=itemslist.gc_range_,
            #
            # Database params:
            root_dir_=itemslist.root_dir_,
            database_=itemslist.database_,
            year_filter_=itemslist.year_filter_,
            custom_items_=itemslist.custom_items_,
            cited_by_filter_=itemslist.cited_by_filter_,
            filters_=itemslist.filters_,
        )
        self.ranking_chart_ = fig


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

    #
    # Main code
    #

    table = itemslist.items_list_.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    if metric_label is None:
        metric_label = itemslist.metric_.replace("_", " ").upper()

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

    ranking_chart_ = RankingChart(
        itemslist=itemslist,
        fig=fig,
    )

    return ranking_chart_
