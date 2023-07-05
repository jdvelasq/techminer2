# flake8: noqa
# pylint: disable=line-too-long
"""
.. _column_chart:

Column chart
===============================================================================

Displays a vertical bar graph of the selected items in a ItemLlist object. 
Items in your list are the X-axis, and the number of records are the Y-axis.

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
...     .column_chart(
...         title="Most Frequent Author Keywords",
...     )
...     .write_html("sphinx/_static/column_chart_0.html")
... )


.. raw:: html

    <iframe src="../_static/column_chart_0.html" height="600px" width="100%" frameBorder="0"></iframe>



* Functional interface


>>> itemslist = tm2p.list_items(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )
>>> tm2p.column_chart(
...     itemslist, 
...     title="Most Frequent Author Keywords",
... ).write_html("sphinx/_static/column_chart_1.html")


.. raw:: html

    <iframe src="../_static/column_chart_1.html" height="600px" width="100%" frameBorder="0"></iframe>


"""


import plotly.express as px
import plotly.graph_objs as go


def column_chart(
    #
    # CHART PARAMS:
    list_items,
    title=None,
    metric_label=None,
    field_label=None,
):
    """Column chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        metric_label (str, optional): Metric label. Defaults to None.
        field_label (str, optional): Field label. Defaults to None.

    Returns:
        BasicChart: A basic chart object.


    """
    metric_label = (
        list_items.metric.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        list_items.field.replace("_", " ").upper()
        if field_label is None
        else field_label
    )

    fig = px.bar(
        list_items.df_,
        x=None,
        y=list_items.metric,
        hover_data=list_items.df_.columns.to_list(),
        orientation="v",
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker_color="rgb(171,171,171)",
        marker_line={"color": "darkslategray"},
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
