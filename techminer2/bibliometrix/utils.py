"""Biblometric indicators by topic



"""

from ..vantagepoint.analyze import list_view
from ..vantagepoint.report import (
    bar_chart,
    cleveland_dot_chart,
    column_chart,
    line_chart,
)


def bbx_indicators_by_item(
    field,
    root_dir="./",
    database="documents",
    metric="OCC",
    # Plot options:
    plot="cleveland_dot_chart",
    metric_label=None,
    field_label=None,
    title=None,
    # Item filters:
    top_n=20,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the number of documents by author using the specified plot."""

    obj = list_view(
        field=field,
        root_dir=root_dir,
        database=database,
        metric=metric,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    vantagepoint_chart = {
        "bar_chart": bar_chart,
        "cleveland_dot_chart": cleveland_dot_chart,
        "column_chart": column_chart,
        "line_chart": line_chart,
    }[plot]

    chart = vantagepoint_chart(
        obj,
        title=title,
        metric_label=metric_label,
        field_label=field_label,
    )

    return chart
