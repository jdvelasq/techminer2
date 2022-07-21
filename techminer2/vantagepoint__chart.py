"""Most frequent items in a databases"""

from .bar_plot import bar_plot
from .cleveland_plot import cleveland_plot
from .column_plot import column_plot
from .line_plot import line_plot
from .vantagepoint__list_view import vantagepoint__list_view
from .pie_plot import pie_plot
from .treemap_plot import treemap_plot
from .wordcloud import wordcloud


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
        "wordcloud": wordcloud,
    }[plot]

    return plot_function(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
