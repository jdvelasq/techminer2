# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _list_items_table:

List Items Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.list_items_table(
...    field='author_keywords',
...    root_dir=root_dir,
... ).head()
                       rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
author_keywords                                ...                           
REGTECH                       1        1   28  ...      9.0      4.0     1.29
FINTECH                       2        2   12  ...      5.0      3.0     0.83
REGULATORY_TECHNOLOGY         3        8    7  ...      4.0      2.0     1.00
COMPLIANCE                    4       12    7  ...      3.0      2.0     0.60
REGULATION                    5        4    5  ...      2.0      2.0     0.33
<BLANKLINE>
[5 rows x 18 columns]


"""

from ...._filtering_lib import generate_custom_items
from ...._sorting_lib import sort_indicators_by_metric
from ....techminer.metrics.global_indicators_by_field import (
    global_indicators_by_field,
)


def list_items_table(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # ITEM FILTERS:
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
    """Returns a dataframe with the extracted items of database field."""

    #
    # MAIN CODE:
    #

    data_frame = global_indicators_by_field(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = sort_indicators_by_metric(data_frame, metric)

    if custom_items is None:
        if metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(data_frame, "OCC"),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    data_frame, "global_citations"
                ),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [
                item
                for item in custom_items_gc
                if item not in custom_items_occ
            ]

        else:
            custom_items = generate_custom_items(
                indicators=data_frame,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    data_frame = data_frame[data_frame.index.isin(custom_items)]

    return data_frame
