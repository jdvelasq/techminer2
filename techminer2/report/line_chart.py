# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Line Chart
===============================================================================

>>> from techminer2.report import line_chart
>>> chart = line_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
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
>>> chart.fig_.write_html("sphinx/_static/report/line_chart.html")

.. raw:: html

    <iframe src="../../../_static/report/line_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> chart.df_.head()
                      rank_occ  OCC  ...  between_2018_2019  growth_percentage
author_keywords                      ...                                      
FINTECH                      1   31  ...                 18              58.06
INNOVATION                   2    7  ...                  1              14.29
FINANCIAL_SERVICES           3    4  ...                  3              75.00
FINANCIAL_TECHNOLOGY         4    4  ...                  3              75.00
BUSINESS                     5    3  ...                  3             100.00
<BLANKLINE>
[5 rows x 5 columns]

>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...
    

"""
import plotly.express as px

from ..metrics.performance_metrics import performance_metrics

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def line_chart(
    #
    # ITEMS PARAMS:
    field,
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
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

    :meta private:
    """

    items = performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        metric=metric,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    metric_label = (
        metric.replace("_", " ").upper() if metric_label is None else metric_label
    )

    field_label = (
        field.replace("_", " ").upper() if field_label is None else field_label
    )

    data_frame = items.df_.copy()

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
        marker=dict(size=9, line={"color": "#465c6b", "width": 2}),
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

    items.fig_ = fig

    return items
