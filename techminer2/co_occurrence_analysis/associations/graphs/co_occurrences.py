# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _co_occurrence_analysis.associations.graphs.co_occurrences:

Co-occurrences
===============================================================================


>>> from techminer2.co_occurrence_analysis.associations.graphs import co_occurrences
>>> co_occurrences(
...     #
...     # FUNCTION PARAMS:
...     item='REGTECH',
...     #
...     # CO-OCC PARAMS:
...     columns='author_keywords',
...     rows=None,
...     #
...     # COLUMN PARAMS:
...     col_top_n=20,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # CHART:
...     title=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence_analysis/associations/co_occurrences.html")

.. raw:: html

    <iframe src="../../../../../../_static/co_occurrence_analysis/associations/co_occurrences.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px

from ..item_associations import item_associations

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def co_occurrences(
    #
    # FUNCTION PARAMS:
    item,
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # CHART:
    title=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """
    associations = item_associations(
        #
        # FUNCTION PARAMS:
        item=item,
        #
        # CO-OCC PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    associations = associations.df_.copy()
    associations["occ"] = associations.index.copy()
    associations["occ"] = associations["occ"].str.split(" ")
    associations["occ"] = associations["occ"].str[-1]
    associations["occ"] = associations["occ"].str.split(":")
    associations["gc"] = associations["occ"].str[1]
    associations["occ"] = associations["occ"].str[0]

    associations["percentage"] = associations.iloc[:, 0] / associations["occ"].astype(float) * 100
    associations["percentage"] = associations["percentage"].round(2)
    associations["name"] = associations.index.copy()

    associations = associations.sort_values(
        by=["percentage", "occ", "gc", "name"], ascending=[False, False, False, True]
    )

    if title is None:
        title = f"(%) Co-occurrences with '{item}'"

    metric_label = "(%) OCC"

    if rows is None:
        field_label = columns.replace("_", " ").upper()
    else:
        field_label = rows.replace("_", " ").upper()

    data_frame = associations.copy()

    fig = px.bar(
        data_frame,
        x="percentage",
        y=None,
        hover_data=data_frame.columns.to_list(),
        orientation="h",
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_traces(
        marker_color=MARKER_COLOR,
        marker_line={"color": MARKER_LINE_COLOR},
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title_text=metric_label,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
        title_text=field_label,
    )

    return fig
