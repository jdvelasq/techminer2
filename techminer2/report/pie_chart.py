# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Pie Chart
===============================================================================

>>> from techminer2.report import pie_chart
>>> chart = pie_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     hole=0.4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> # chart.fig_.write_html("sphinx/_static/report/pie_chart.html")

.. raw:: html

    <iframe src="../_static/report/pie_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                      rank_occ  OCC
author_keywords                    
FINTECH                      1   31
INNOVATION                   2    7
FINANCIAL_SERVICES           3    4
FINANCIAL_INCLUSION          4    3
FINANCIAL_TECHNOLOGY         5    3

>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
import plotly.express as px

from ..metrics.performance_metrics import performance_metrics


def pie_chart(
    #
    # ITEMS PARAMS:
    field,
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    hole=0.4,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a pie chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        hole (float, optional): Hole size. Defaults to 0.4.

    Returns:
        BasicChart: A BasicChart object.

    :meta private:
    """

    items = performance_metrics(
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

    data_frame = items.df_.copy()

    fig = px.pie(
        data_frame,
        values=metric,
        names=data_frame.index.to_list(),
        hole=hole,
        hover_data=data_frame.columns.to_list(),
        title=title if title is not None else "",
    )
    fig.update_traces(textinfo="percent+value")
    fig.update_layout(legend={"y": 0.5})

    items.fig_ = fig

    return items
