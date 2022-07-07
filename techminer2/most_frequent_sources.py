"""
Most frequent sources (in main documents database)
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/most_frequent_sources.html"

>>> most_frequent_sources(
...     directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .most_frequent_items import most_frequent_items


def most_frequent_sources(
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="cleveland",
):
    """Plots the number of documents by source using the specified plot."""

    return most_frequent_items(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        title="Most Frequent Sources",
        plot=plot,
        database="documents",
    )

    # if database == "documents":
    #     title = "Most Frequent Sources"
    # elif database == "references":
    #     title = "Most Frequent Sources in References"
    # elif database == "cited_by":
    #     title = "Most Frequent Sources in Citing Documents"
    # else:
    #     raise ValueError(
    #         "Invalid database name. Database must be one of: 'documents', 'references', 'cited_by'"
    #     )

    # indicators = terms_list(
    #     column="source_abbr",
    #     metric="OCC",
    #     top_n=top_n,
    #     min_occ=min_occ,
    #     max_occ=max_occ,
    #     directory=directory,
    #     database=database,
    # )

    # plot_function = {
    #     "bar": bar_chart,
    #     "column": column_chart,
    #     "line": line_chart,
    #     "circle": pie_chart,
    #     "cleveland": cleveland_chart,
    #     "wordcloud": word_cloud,
    # }[plot]

    # return plot_function(
    #     dataframe=indicators,
    #     metric="OCC",
    #     title=title,
    # )
