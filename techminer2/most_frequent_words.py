"""
Most Frequent Words (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_frequent_words.png"
>>> most_frequent_words(
...     'author_keywords', 
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_frequent_words.png
    :width: 700px
    :align: center

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_frequent_words(column="author_keywords", directory="./", top_n=20):

    indicators = column_indicators(column=column, directory=directory)
    indicators = indicators.sort_values(
        by=["num_documents", "global_citations", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.num_documents,
        y=indicators.index,
        title="Most frequent words",
        text=indicators.num_documents,
        xlabel="Num Documents",
        ylabel=column.replace("_", " ").title(),
    )

    # fig = px.scatter(
    #     x=indicators.num_documents,
    #     y=indicators.index,
    #     title="Most frequent words",
    #     text=indicators.num_documents,
    #     labels={"x": "Num Documents", "y": "Institution Name"},
    # )
    # fig.update_traces(marker=dict(size=10, color="black"))
    # fig.update_traces(textposition="middle right")
    # fig.update_traces(line=dict(color="black"))
    # fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    # fig.update_yaxes(
    #     linecolor="gray",
    #     linewidth=2,
    #     gridcolor="lightgray",
    #     autorange="reversed",
    #     griddash="dot",
    # )

    # return fig
