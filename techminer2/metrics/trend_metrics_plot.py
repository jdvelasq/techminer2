# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Trend Metrics Plot
===============================================================================


>>> from techminer2.metrics import trend_metrics_plot
>>> plot = trend_metrics_plot(
...     #
...     # TABLE PARAMS:
...     selected_columns=[
...         "OCC",
...         "global_citations",
...         "mean_global_citations",
...         "mean_global_citations_per_year",
...     ],
...     #
...     # CHART PARAMS:
...     metric_to_plot="OCC",
...     auxiliary_metric_to_plot=None,
...     title="Annual Scientific Production",
...     year_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> # plot.write_html("sphinx/_static/metrics/trend_metrics.html")

.. raw:: html

    <iframe src="../_static/metrics/trend_metrics.html"  
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from ._plot_trend_metrics import plot_trend_metrics
from .trend_metrics_frame import trend_metrics_frame

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def trend_metrics_plot(
    #
    # TABLE PARAMS:
    selected_columns=None,
    #
    # CHART PARAMS:
    metric_to_plot="OCC",
    auxiliary_metric_to_plot=None,
    title=None,
    year_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    data_frame = trend_metrics_frame(
        #
        # TABLE PARAMS:
        selected_columns=selected_columns,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Plot
    fig = plot_trend_metrics(
        #
        # METRICS:
        data_frame=data_frame,
        metric_to_plot=metric_to_plot,
        auxiliary_metric_to_plot=auxiliary_metric_to_plot,
        #
        # CHART PARAMS:
        title=title,
        year_label=year_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
    )

    return fig
