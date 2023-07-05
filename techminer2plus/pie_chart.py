# flake8: noqa
# pylint: disable=line-too-long
"""
.. _pie_chart:

Pie Chart
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .list_items(
...         field='author_keywords',
...         top_n=20,
...     )
...     .pie_chart(
...         title="Most Frequent Author Keywords",
...     )
...     .write_html("sphinx/_static/pie_chart_0.html")
... )

.. raw:: html

    <iframe src="../_static/pie_chart_0.html" height="600px" width="100%" frameBorder="0"></iframe>

    
* Functional interface


>>> itemslist = tm2p.list_items(
...    field='author_keywords',
...    root_dir=root_dir,
...    top_n=20,
... )
>>> tm2p.pie_chart(
...     itemslist, 
...     title="Most Frequent Author Keywords",
... ).write_html("sphinx/_static/pie_chart_1.html")

.. raw:: html

    <iframe src="../_static/pie_chart_1.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
import plotly.express as px


def pie_chart(
    list_items,
    title=None,
    hole=0.4,
):
    """Creates a pie chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        hole (float, optional): Hole size. Defaults to 0.4.

    Returns:
        BasicChart: A BasicChart object.


    """

    fig = px.pie(
        list_items.df_,
        values=list_items.metric,
        names=list_items.df_.index.to_list(),
        hole=hole,
        hover_data=list_items.df_.columns.to_list(),
        title=title if title is not None else "",
    )
    fig.update_traces(textinfo="percent+value")
    fig.update_layout(legend={"y": 0.5})

    return fig
