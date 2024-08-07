# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Cleveland Dot Chart
===============================================================================

>>> from techminer2.report import cleveland_dot_chart
>>> chart = cleveland_dot_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     metric_label=None,
...     field_label=None,
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> # chart.write_html("sphinx/_static/report/cleveland_dot_chart.html")

.. raw:: html

    <iframe src="../_static/report/cleveland_dot_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px  # type: ignore

from ..metrics.performance_metrics_frame import performance_metrics_frame

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
    custom_terms=None,
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

    :meta private:
    """

    items = performance_metrics_frame(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
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

    data_frame = items.copy()

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

    return fig
