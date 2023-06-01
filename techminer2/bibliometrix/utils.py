"""Biblometric indicators by topic



"""


from ..vantagepoint.report import ranking_chart


# pylint: disable=too-many-arguments
def bbx_generic_indicators_by_item(
    fnc_view,
    field,
    root_dir="./",
    database="documents",
    metric="OCC",
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
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

    chart = ranking_chart(
        obj,
        title=title,
        metric_label=metric_label,
        field_label=field_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )

    return chart
