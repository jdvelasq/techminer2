# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _cleveland_dot_chart:

Cleveland Dot Chart
===============================================================================

>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> report = vantagepoint.report.cleveland_dot_chart(
...    field='author_keywords',
...    title="Most Frequent Author Keywords",
...    top_n=20,
...    root_dir=root_dir,
... )
>>> report.fig_.write_html("sphinx/_static/vantagepoint/report/cleveland_dot_chart.html")

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/report/cleveland_dot_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from ..discover.list_items import list_items

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def cleveland_dot_chart(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    metric_label=None,
    field_label=None,
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
    """Creates a cleveland doc chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.

    Returns:
        BasicChart: A basic chart object.

    """

    items = list_items(
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

    metric_label = metric.replace("_", " ").upper() if metric_label is None else metric_label

    field_label = field.replace("_", " ").upper() if field_label is None else field_label

    data_frame = items.df_.copy()

    fig = px.scatter(
        data_frame,
        x=metric,
        y=None,
        hover_data=data_frame.columns.to_list(),
        size=metric,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker=dict(
            size=12,
            line=dict(color=MARKER_LINE_COLOR, width=2),
        ),
        marker_color=MARKER_COLOR,
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

    items.fig_ = fig

    return items
