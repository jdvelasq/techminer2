"""Biblometric indicators by topic



"""

from ..classes import BasicChart
from ..item_utils import generate_custom_items
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators import impact_indicators_by_item
from ..utils import check_impact_metric, check_integer, check_integer_range
from ..vantagepoint.analyze import list_view
from ..vantagepoint.report import (
    bar_chart,
    cleveland_dot_chart,
    column_chart,
    line_chart,
)


# pylint: disable=too-many-arguments
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


# pylint: disable=too-many-arguments
def item_impact(
    field,
    impact_measure="h_index",
    root_dir="./",
    database="documents",
    # Plot options:
    plot="cleveland_dot_chart",
    title=None,
    impact_measure_label=None,
    field_label=None,
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
    """computes local impact by <field>"""

    check_integer(top_n)
    check_integer_range(occ_range)
    check_integer_range(gc_range)
    check_impact_metric(impact_measure)

    indicators = impact_indicators_by_item(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, impact_measure)

    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    column_names = {
        column: column.replace("_", " ").title()
        for column in indicators.columns
    }
    indicators = indicators.rename(columns=column_names)
    indicators = indicators.rename(
        columns={
            "H Index": "H-Index",
            "G Index": "G-Index",
            "M Index": "M-Index",
            "Occ": "OCC",
        }
    )

    ###

    obj = _ImpactIndicators()
    obj.table_ = indicators
    obj.criterion_ = field
    obj.metric_ = (
        impact_measure.replace("h_index", "H-Index")
        .replace("g_index", "G-Index")
        .replace("m_ndex", "M-Index")
        .replace("Occ", "OCC")
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
        metric_label=impact_measure_label,
        field_label=field_label,
    )

    return chart
