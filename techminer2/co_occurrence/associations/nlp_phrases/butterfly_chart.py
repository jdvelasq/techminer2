# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Butterfly Chart
===============================================================================


>>> from techminer2.co_occurrence.associations.nlp_phrases import butterfly_chart
>>> chart = butterfly_chart(
...     #
...     # FUNCTION PARAMS:
...     item_a="REGULATORY_TECHNOLOGY",
...     item_b="FINANCIAL_REGULATION",
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
... ).write_html("sphinx/_static/co_occurrence/associations/nlp_phrases/butterfly_chart.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence/associations/nlp_phrases/butterfly_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ....butterfly_chart import butterfly_chart as __butterfly_chart

ROWS_AND_COLUMNS = "nlp_phrases"


def butterfly_chart(
    #
    # FUNCTION PARAMS:
    item_a,
    item_b,
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

    return __butterfly_chart(
        #
        # FUNCTION PARAMS:
        item_a=item_a,
        item_b=item_b,
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
