"""Most global cited items in a databases"""

from .bar_plot import bar_plot
from .cleveland_plot import cleveland_plot
from .column_plot import column_plot
from .line_plot import line_plot
from .pie_plot import pie_plot
from .list_view import list_view
from .word_cloud import word_cloud


def most_global_cited_items(
    column,
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title=None,
    plot="bar",
    database="documents",
):
    """Plots the number of documents by source using the specified plot."""

    indicators = list_view(
        column=column,
        metric="global_citations",
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
        "wordcloud": word_cloud,
    }[plot]

    return plot_function(
        dataframe=indicators,
        metric="global_citations",
        title=title,
    )
