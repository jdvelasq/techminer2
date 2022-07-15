"""
Most Frequent Abstract Words
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_frequent_abstract_words.html"

>>> most_frequent_abstract_words(
...     directory=directory,
...     top_n=20,
...     min_occ=None,
...     max_occ=None,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/most_frequent_abstract_words.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_plot import bar_plot
from .cleveland_plot import cleveland_plot
from .column_plot import column_plot
from .line_plot import line_plot
from .pie_plot import pie_plot
from .list_view import list_view
from .wordcloud import wordcloud


def most_frequent_abstract_words(
    column="author_keywords",
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    plot="bar",
    database="documents",
):
    """Plot the most frequent words."""

    if database == "documents":
        title = "Most Frequent " + column.replace("_", " ").title()
    elif database == "references":
        title = "Most Frequent " + column.replace("_", " ").title() + " in References"
    elif database == "cited_by":
        title = (
            "Most Frequent " + column.replace("_", " ").title() + " in Citing documents"
        )
    else:
        raise ValueError(
            "Invalid database name. Database must be one of: 'documents', 'references', 'cited_by'"
        )

    indicators = list_view(
        column="abstract_words",
        metric="OCC",
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database=database,
    )

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "circle": pie_chart,
        "cleveland": cleveland_chart,
        "wordcloud": wordcloud,
    }[plot]

    return plot_function(
        dataframe=indicators,
        metric="OCC",
        title=title,
    )
