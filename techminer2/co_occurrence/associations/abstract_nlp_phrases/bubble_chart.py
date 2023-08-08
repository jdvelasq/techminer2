# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bubble Chart
===============================================================================


>>> from techminer2.co_occurrence.associations.abstract_nlp_phrases import bubble_chart
>>> chart = bubble_chart(
...     #
...     # CHART PARAMS:
...     title=None,
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence/associations/abstract_nlp_phrases/bubble_chart.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence/associations/abstract_nlp_phrases/bubble_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ....bubble_chart import bubble_chart as __bubble_chart

ROWS_AND_COLUMNS = "abstract_nlp_phrases"


def bubble_chart(
    #
    # CHART PARAMS:
    title=None,
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

    return __bubble_chart(
        #
        # FUNCTION PARAMS:
        columns=ROWS_AND_COLUMNS,
        rows=None,
        #
        # CHART PARAMS:
        title=title,
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
