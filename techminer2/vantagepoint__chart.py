"""Most frequent items in a databases"""

from ._plots.bar_plot import bar_plot
from ._plots.cleveland_plot import cleveland_plot
from ._plots.column_plot import column_plot
from ._plots.line_plot import line_plot
from .vantagepoint__list_view import vantagepoint__list_view
from ._plots.pie_plot import pie_plot
from ._plots.treemap_plot import treemap_plot
from .vantagepoint__word_cloud import vantagepoint__word_cloud


def vantagepoint__chart(
    column,
    directory="./",
    top_n=20,
    min_occ=None,
    max_occ=None,
    title=None,
    plot="bar",
    database="documents",
    metric="OCC",
):
    """Plots the number of documents by source using the specified plot."""

    indicators = vantagepoint__list_view(
        column=column,
        metric=metric,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database=database,
    )

    plot_function = {
        "bar": bar_plot,
        "cleveland": cleveland_plot,
        "column": column_plot,
        "line": line_plot,
        "pie": pie_plot,
        "treemap": treemap_plot,
        "wordcloud": vantagepoint__word_cloud,
    }[plot]

    return plot_function(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
