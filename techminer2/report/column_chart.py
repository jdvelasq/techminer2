# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Column Chart
===============================================================================

>>> from techminer2.report import column_chart
>>> chart = column_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     metric_label=None,
...     field_label=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> # chart.write_html("sphinx/_static/report/column_chart.html")

.. raw:: html

    <iframe src="../_static/report/column_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px  # type: ignore

from ..metrics.performance_metrics_frame import performance_metrics_frame

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def column_chart(
    #
    # ITEMS PARAMS:
    field,
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    metric_label=None,
    field_label=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    items = performance_metrics_frame(
        #
        # ITEMS PARAMS:
        field=field,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        metric=metric,
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

    fig = px.bar(
        data_frame,
        x=None,
        y=metric,
        hover_data=data_frame.columns.to_list(),
        orientation="v",
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker_color=MARKER_COLOR,
        marker_line={"color": MARKER_LINE_COLOR},
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
