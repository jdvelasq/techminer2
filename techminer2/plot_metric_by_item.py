"""Make a plot of a metric by item."""

from .tm2.plots.bar_plot import bar_plot
from .tm2.plots.cleveland_plot import cleveland_plot
from .tm2.plots.column_plot import column_plot
from .tm2.plots.line_plot import line_plot
from .tm2.plots.pie_plot import pie_plot
from .vp.report.wordcloud import wordcloud


def plot_metric_by_item(
    column,
    metric,
    directory,
    top_n,
    min_occ,
    max_occ,
    title,
    plot,
    file_name,
):
    """Plots the number of documents by source using the specified plot."""

    plot_function = {
        "bar": bar_chart,
        "column": column_chart,
        "line": line_chart,
        "pie": pie_chart,
        "cleveland": cleveland_chart,
        "wordcloud": wordcloud,
    }[plot]

    return plot_function(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
        title=title,
        file_name=file_name,
    )
