"""Most frequent items in a databases"""

from .tm2.plots.bar_plot import bar_plot
from .tm2.plots.cleveland_plot import cleveland_plot
from .tm2.plots.column_plot import column_plot
from .tm2.plots.line_plot import line_plot
from .tm2.plots.pie_plot import pie_plot
from .vantagepoint.analyze.list_view import list_view
from .wordcloud import wordcloud


def chart(
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

    indicators = list_view(
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
        "column": column_plot,
        "line": line_plot,
        "pie": pie_plot,
        "cleveland": cleveland_plot,
        "wordcloud": wordcloud,
    }[plot]

    return plot_function(
        dataframe=indicators,
        metric=metric,
        title=title,
    )
