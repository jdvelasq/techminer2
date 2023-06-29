# flake8: noqa
# pylint: disable=line-too-long
"""
.. _bar_chart:

Bar Chart
===============================================================================

Displays a horizontal bar graph of the selected items in a ItemLlist object. 
Items in your list are the Y-axis, and the number of records are the X-axis.



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bar_chart.html"

>>> import techminer2plus as tm2p
>>> (
...     tm2p.Records(root_dir=root_dir) 
...     .field("author_keywords", top_n=10) 
...     .bar_chart(title="Most Frequent Author Keywords")
...     .write_html(file_name)
... )


.. raw:: html

    <iframe src="../_static/bar_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


def bar_chart(
    data,
    #
    # Chart params:
    title=None,
    metric_label=None,
    field_label=None,
):
    """Bar chart."""

    metric_label = (
        data.metric_.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        data.field_.replace("_", " ").upper()
        if field_label is None
        else field_label
    )

    fig = px.bar(
        data.frame_,
        x=data.metric_,
        y=None,
        hover_data=data.frame_.columns.to_list(),
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
