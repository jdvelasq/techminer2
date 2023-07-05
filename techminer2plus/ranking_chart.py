# flake8: noqa
# pylint: disable=line-too-long
"""
.. _ranking_chart:

Ranking Chart
===============================================================================

Default visualization chart for Bibliometrix.


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
...     .ranking_chart(
...         title="Most Frequent Author Keywords",
...     )
...     .write_html("sphinx/_static/ranking_chart_0.html")
... )

.. raw:: html

    <iframe src="../_static/ranking_chart_0.html" height="600px" width="100%" frameBorder="0"></iframe>

* Functional interface

>>> list_items = tm2p.list_items(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )
>>> tm2p.ranking_chart(
...    list_items=list_items,
...    title="Most Frequent Author Keywords"
... ).write_html("sphinx/_static/ranking_chart_1.html")



.. raw:: html

    <iframe src="../_static/ranking_chart_1.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


# pylint: disable=too-many-arguments
def ranking_chart(
    list_items,
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
):
    """Creates a rank chart."""

    metric_label = (
        list_items.metric.replace("_", " ").upper()
        if metric_label is None
        else metric_label
    )

    field_label = (
        list_items.field.replace("_", " ").upper() + " RANKING"
        if field_label is None
        else field_label
    )

    table = list_items.df_.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y=list_items.metric,
        hover_data=list_items.df_.columns.to_list(),
        markers=True,
    )

    fig.update_traces(
        marker={
            "size": marker_size,
            "line": {"color": line_color, "width": 0},
        },
        marker_color=line_color,
        line={"color": line_color, "width": line_width},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=metric_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=field_label,
    )

    for name, row in table.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row[list_items.metric],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return fig
