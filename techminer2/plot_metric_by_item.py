"""Make a plot of a metric by item."""

from .bar_chart import bar_chart
from .circle_chart import circle_chart
from .cleveland_chart import cleveland_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .word_cloud import word_cloud


def plot_metric_by_item(
    column,
    metric,
    directory,
    top_n,
    min_occ,
    max_occ,
    title,
    plot,
):
    """Plots the number of documents by source using the specified plot."""

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "circle": circle_chart,
        "cleveland": cleveland_chart,
        "wordcloud": word_cloud,
    }[plot]

    return plot_function(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        title=title,
    )
