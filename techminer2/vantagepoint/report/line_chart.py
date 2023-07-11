# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _line_chart:

Line Chart
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.line_chart(
...    field='author_keywords',
...    title="Most Frequent Author Keywords",
...    top_n=20,
...    root_dir=root_dir,
... ).write_html("sphinx/_static/line_chart.html")

.. raw:: html

    <iframe src="../../../../_static/line_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

# from ..analyze.discover.list_items_table import list_items_table

MARKER_COLOR = "#8da4b4"
MARKER_LINE_COLOR = "#556f81"


def line_chart(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
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

    data_frame = list_items_table(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    metric_label = (
        metric.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        field.replace("_", " ").upper() if field_label is None else field_label
    )

    fig = px.line(
        data_frame,
        x=None,
        y=metric,
        hover_data=data_frame.columns.to_list(),
        markers=True,
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title,
    )
    fig.update_traces(
        marker=dict(size=9, line={"color": "#556f81", "width": 2}),
        marker_color=MARKER_COLOR,
        line={"color": MARKER_LINE_COLOR},
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

    return fig
