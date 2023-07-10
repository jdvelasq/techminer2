# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _pie_chart:

Pie Chart
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p
>>> tm2p.pie_chart(
...    field='author_keywords',
...    title="Most Frequent Author Keywords",
...    top_n=20,
...    root_dir=root_dir,
... ).write_html("sphinx/_static/pie_chart.html")

.. raw:: html

    <iframe src="../../../../_static/pie_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px

from .list_items_table import list_items_table


def pie_chart(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    title=None,
    hole=0.4,
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
    """Creates a pie chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        hole (float, optional): Hole size. Defaults to 0.4.

    Returns:
        BasicChart: A BasicChart object.


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

    return fig
