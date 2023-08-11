# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _tm2.co_occurrence.associations.author_keywords.cosine_similarities_graph:

Cosine Similarities Graph
===============================================================================


>>> from techminer2.co_occurrence.associations.author_keywords import cosine_similarities_graph
>>> cosine_similarities_graph(
...     #
...     # FUNCTION PARAMS:
...     item="REGTECH",
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
... ).write_html("sphinx/_static/co_occurrence/associations/keywords/cosine_similarities_graph.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence/associations/keywords/cosine_similarities_graph.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ....cosine_similarities_graph import cosine_similarities_graph as __cosine_similarities_graph

ROWS_AND_COLUMNS = "keywords"


def cosine_similarities_graph(
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

    return __cosine_similarities_graph(
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
