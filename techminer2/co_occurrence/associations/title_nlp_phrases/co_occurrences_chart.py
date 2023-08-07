# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Co-occurrences Chart
===============================================================================


>>> from techminer2.co_occurrence.associations.title_nlp_phrases import co_occurrences_chart
>>> co_occurrences_chart(
...     #
...     # FUNCTION PARAMS:
...     item="REGULATORY_TECHNOLOGY",
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     y_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence/associations/title_nlp_phrases/co_occurrences_chart.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence/associations/title_nlp_phrases/co_occurrences_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ....co_occurrences_chart import co_occurrences_chart as __co_occurrences_chart

ROWS_AND_COLUMNS = "title_nlp_phrases"


def co_occurrences_chart(
    #
    # FUNCTION PARAMS:
    item,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    y_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
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

    return __co_occurrences_chart(
        #
        # FUNCTION PARAMS:
        item,
        columns=ROWS_AND_COLUMNS,
        rows=None,
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        y_label=y_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # ROW PARAMS:
        row_top_n=None,
        row_occ_range=(None, None),
        row_gc_range=(None, None),
        row_custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
