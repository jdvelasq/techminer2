# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _item_associations_table:

Item Associations Table
===============================================================================

Computes the associations of a item in a co-occurrence matrix.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> tm2.item_associations_table(
...    item='REGTECH',
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
                                REGTECH 28:329
author_keywords                               
FINTECH 12:249                              12
COMPLIANCE 07:030                            7
REGULATION 05:164                            4
FINANCIAL_SERVICES 04:168                    3
SUPTECH 03:004                               3
REGULATORY_TECHNOLOGY 07:037                 2
FINANCIAL_REGULATION 04:035                  2
ARTIFICIAL_INTELLIGENCE 04:023               2
RISK_MANAGEMENT 03:014                       2
BLOCKCHAIN 03:005                            2
SEMANTIC_TECHNOLOGIES 02:041                 2
DATA_PROTECTION 02:027                       2
SMART_CONTRACTS 02:022                       2
CHARITYTECH 02:017                           2
ENGLISH_LAW 02:017                           2
ACCOUNTABILITY 02:014                        2
DATA_PROTECTION_OFFICER 02:014               2
ANTI_MONEY_LAUNDERING 05:034                 1
INNOVATION 03:012                            1


"""
# from .vantagepoint.discover.matrix.co_occurrence_matrix import (
#     co_occurrence_matrix,
# )


def item_associations_table(
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
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Computes the associations of a item in a co-occurrence matrix."""

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    def extract_item_column_from_coc_matrix(obj, pos, name):
        matrix = obj.copy()
        series = matrix.iloc[:, pos]
        series = series.drop(labels=[name], axis=0, errors="ignore")
        series = series[series > 0]
        series.index.name = obj.index.name
        return series

    #
    # MAIN CODE:
    #

    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
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

    pos, name = extract_item_position_and_name(cooc_matrix.columns, item)
    series = extract_item_column_from_coc_matrix(cooc_matrix, pos, name)
    frame = series.to_frame()
    frame["OCC"] = [text.split(" ")[-1].split(":")[0] for text in frame.index]
    frame["GC"] = [text.split(" ")[-1].split(":")[-1] for text in frame.index]
    frame["NAME"] = [" ".join(text.split(" ")[:-1]) for text in frame.index]
    frame = frame.sort_values(
        by=[name, "OCC", "GC", "NAME"], ascending=[False, False, False, True]
    )
    series = frame[[name]]

    return series
