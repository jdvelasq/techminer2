# flake8: noqa
# pylint: disable=line-too-long
"""
.. _cleveland_dot_chart:

Cleveland Dot Chart
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
...     .cleveland_dot_chart(
...         title="Most Frequent Author Keywords",
...     )
...     .write_html("sphinx/_static/cleveland_chart_0.html")
... )

.. raw:: html

    <iframe src="../_static/cleveland_chart_0.html" height="600px" width="100%" frameBorder="0"></iframe>

    
* Functional interface

>>> list_items = tm2p.list_items(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
... )
>>> tm2p.cleveland_dot_chart(
...    list_items=list_items,
...    title="Most Frequent Author Keywords"
... ).write_html("sphinx/_static/cleveland_chart_1.html")

.. raw:: html

    <iframe src="../_static/cleveland_chart_1.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


def cleveland_dot_chart(
    list_items=None,
    title=None,
    metric_label=None,
    field_label=None,
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

    fig = px.scatter(
        list_items.df_,
        x=list_items.metric,
        y=None,
        hover_data=list_items.df_.columns.to_list(),
        size=list_items.metric,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker=dict(
            size=12,
            line=dict(color="black", width=2),
        ),
        marker_color="slategray",
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
