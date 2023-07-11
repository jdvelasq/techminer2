# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_relevant_authors_chart:

Most Relevant Authors Chart
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p
>>> tm2p.most_relevant_authors_chart(
...    title="Most Frequent Authors",
...    top_n=20,
...    root_dir=root_dir,
... ).write_html("sphinx/_static/most_relevant_authors_chart.html")

.. raw:: html

    <iframe src="../../../../../../_static/most_relevant_authors_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .list_items_table import list_items_table

MARKER_COLOR = "#8da4b4"
MARKER_LINE_COLOR = "#556f81"
FIELD = "authors"
METRIC = "OCCGC"


def most_relevant_authors_chart(
    #
    # ITEM FILTERS:
    top_n=None,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a rank chart."""

    data_frame = list_items_table(
        #
        # ITEMS PARAMS:
        field=FIELD,
        metric=METRIC,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    metric = METRIC

    if metric == "OCCGC":
        metric = "OCC"

    metric_label = (
        metric.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        FIELD.replace("_", " ").upper() + " RANKING"
        if field_label is None
        else field_label
    )

    table = data_frame.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y=metric,
        hover_data=data_frame.columns.to_list(),
        markers=True,
    )

    fig.update_traces(
        marker={
            "size": marker_size,
            "line": {"color": MARKER_LINE_COLOR, "width": 1},
        },
        marker_color=MARKER_COLOR,
        line={"color": MARKER_LINE_COLOR, "width": line_width},
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
            y=row[metric],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
