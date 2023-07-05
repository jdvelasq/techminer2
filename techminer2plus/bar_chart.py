# flake8: noqa
# pylint: disable=line-too-long
"""
.. _bar_chart:

Bar Chart
===============================================================================

Displays a horizontal bar graph of the selected items in a ItemLlist object. 
Items in your list are the Y-axis, and the number of records are the X-axis.

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
...     .bar_chart(
...         title="Most Frequent Author Keywords",
...     )
...     .write_html("sphinx/_static/bar_chart_0.html")
... )

.. raw:: html

    <iframe src="../_static/bar_chart_0.html" height="600px" width="100%" frameBorder="0"></iframe>

* Functional interface

>>> list_items = tm2p.list_items(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
... )
>>> tm2p.bar_chart(
...    list_items=list_items,
...    title="Most Frequent Author Keywords"
... ).write_html("sphinx/_static/bar_chart_1.html")


.. raw:: html

    <iframe src="../_static/bar_chart_1.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=invalid-name
def bar_chart(
    #
    # CHART PARAMS:
    list_items,
    title=None,
    metric_label=None,
    field_label=None,
):
    """Bar chart."""

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
        x=list_items.metric,
        y=None,
        hover_data=list_items.df_.columns.to_list(),
        orientation="h",
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
        title_text=metric_label,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        title_text=field_label,
    )

    return fig
