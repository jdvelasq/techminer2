"""Biblometric indicators by topic



"""

# from ..item_utils import generate_custom_items
# from ..sort_utils import sort_indicators_by_metric
# from ..techminer.indicators import impact_indicators_by_item
# from ..utils import check_impact_metric, check_integer, check_integer_range
from ..vantagepoint.analyze import impact_view, list_view
from ..vantagepoint.report import (
    bar_chart,
    cleveland_dot_chart,
    column_chart,
    line_chart,
)


# pylint: disable=too-many-arguments
def bbx_generic_indicators_by_item(
    fnc_view,
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
    """Generic function to compute indicators by item."""

    obj = fnc_view(
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


# # pylint: disable=too-many-arguments
# def bbx_indicators_by_item(
#     field,
#     root_dir="./",
#     database="documents",
#     metric="OCC",
#     # Plot options:
#     plot="cleveland_dot_chart",
#     metric_label=None,
#     field_label=None,
#     title=None,
#     # Item filters:
#     top_n=20,
#     occ_range=None,
#     gc_range=None,
#     custom_items=None,
#     # Database filters:
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """Plots the number of documents by author using the specified plot."""

#     return bbx_generic_indicators_by_item(
#         fnc_view=list_view,
#         field=field,
#         root_dir=root_dir,
#         database=database,
#         metric=metric,
#         # Plot options:
#         plot=plot,
#         metric_label=metric_label,
#         field_label=field_label,
#         title=title,
#         # Item filters:
#         top_n=top_n,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         custom_items=custom_items,
#         # Database filters:
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

# obj = list_view(
#     field=field,
#     root_dir=root_dir,
#     database=database,
#     metric=metric,
#     # Item filters:
#     top_n=top_n,
#     occ_range=occ_range,
#     gc_range=gc_range,
#     custom_items=custom_items,
#     # Database filters:
#     year_filter=year_filter,
#     cited_by_filter=cited_by_filter,
#     **filters,
# )

# vantagepoint_chart = {
#     "bar_chart": bar_chart,
#     "cleveland_dot_chart": cleveland_dot_chart,
#     "column_chart": column_chart,
#     "line_chart": line_chart,
# }[plot]

# chart = vantagepoint_chart(
#     obj,
#     title=title,
#     metric_label=metric_label,
#     field_label=field_label,
# )

# return chart


# pylint: disable=too-many-arguments
# def bbx_impact_by_item(
#     field,
#     root_dir="./",
#     database="documents",
#     metric="h_index",
#     # Plot options:
#     plot="cleveland_dot_chart",
#     metric_label=None,
#     field_label=None,
#     title=None,
#     # Item filters:
#     top_n=20,
#     occ_range=None,
#     gc_range=None,
#     custom_items=None,
#     # Database filters:
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """computes local impact by <field>"""

#     return bbx_generic_indicators_by_item(
#         fnc_view=impact_view,
#         field=field,
#         root_dir=root_dir,
#         database=database,
#         metric=metric,
#         # Plot options:
#         plot=plot,
#         metric_label=metric_label,
#         field_label=field_label,
#         title=title,
#         # Item filters:
#         top_n=top_n,
#         occ_range=None,
#         gc_range=None,
#         custom_items=None,
#         # Database filters:
#         year_filter=None,
#         cited_by_filter=None,
#         **filters,
#     )

# obj = impact_view(
#     field=field,
#     root_dir=root_dir,
#     database=database,
#     metric=metric,
#     # Item filters:
#     top_n=top_n,
#     occ_range=occ_range,
#     gc_range=gc_range,
#     custom_items=custom_items,
#     # Database filters:
#     year_filter=year_filter,
#     cited_by_filter=cited_by_filter,
#     **filters,
# )

# vantagepoint_chart = {
#     "bar_chart": bar_chart,
#     "cleveland_dot_chart": cleveland_dot_chart,
#     "column_chart": column_chart,
#     "line_chart": line_chart,
# }[plot]

# chart = vantagepoint_chart(
#     obj,
#     title=title,
#     metric_label=metric_label,
#     field_label=field_label,
# )

# return chart
