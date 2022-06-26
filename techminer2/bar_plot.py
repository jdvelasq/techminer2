"""
Bar plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/bar_plot.html"
>>> dataframe = column_indicators(
...     column="countries",
...     directory=directory,
... ).head(20)

>>> bar_plot(
...     dataframe,
...     column="num_documents",
...     title="Annual Scientific Production",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/bar_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import textwrap

import plotly.express as px

TEXTLEN = 40


def bar_plot(
    dataframe,
    column,
    title=None,
):
    """
    Make a  bar plot from a dataframe.

    :param dataframe: Dataframe
    :param column: Column to plot
    :param title: Title of the plot
    :return: Plotly figure
    """

    x_label = column.replace("_", " ").title()
    y_label = dataframe.index.name.replace("_", " ").title()

    dataframe = dataframe.reset_index()
    names_dict = {col: col.replace("_", " ").title() for col in dataframe.columns}
    dataframe.rename(columns=names_dict, inplace=True)
    dataframe[y_label] = dataframe[y_label].str.title()

    if dataframe.index.dtype != "int64":
        dataframe.index = [
            textwrap.shorten(
                text=text,
                width=TEXTLEN,
                placeholder="...",
                break_long_words=False,
            )
            for text in dataframe.index.to_list()
        ]

    fig = px.bar(
        dataframe,
        x=x_label,
        y=y_label,
        hover_data=dataframe.columns.to_list(),
        title=title,
        orientation="h",
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(
        marker_color="rgb(171,171,171)", marker_line={"color": "darkslategray"}
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    return fig
