# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Term Associations Frame
===============================================================================


## >>> from techminer2.tools.associations import term_associations_frame
## >>> associations = term_associations_frame(
## ...     #
## ...     # FUNCTION PARAMS:
## ...     item='FINTECH',
## ...     #
## ...     # CO-OCC PARAMS:
## ...     columns='author_keywords',
## ...     rows=None,
## ...     #
## ...     # COLUMN PARAMS:
## ...     col_top_n=20,
## ...     col_occ_range=(None, None),
## ...     col_gc_range=(None, None),
## ...     col_custom_terms=None,
## ...     #
## ...     # ROW PARAMS:
## ...     row_top_n=None,
## ...     row_occ_range=(None, None),
## ...     row_gc_range=(None, None),
## ...     row_custom_terms=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> associations.head()
                              FINTECH 31:5168
rows                                         
INNOVATION 07:0911                          5
FINANCIAL_SERVICES 04:0667                  3
FINANCIAL_INCLUSION 03:0590                 3
MARKETPLACE_LENDING 03:0317                 3
FINANCIAL_TECHNOLOGY 03:0461                2


"""
from ...co_occurrence_matrix.co_occurrence_matrix import co_occurrence_matrix
from ...helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes


def term_associations_frame(
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
    col_custom_terms=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

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
        # series = series[series > 0]
        series.index.name = obj.index.name
        return series

    #
    #
    # MAIN CODE:
    #
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
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_terms=row_custom_terms,
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
    frame = frame.sort_values(by=[name, "OCC", "GC", "NAME"], ascending=[False, False, False, True])
    frame = frame[[name]]

    return frame
