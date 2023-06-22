"""Computes the associations of a item in a co-occurrence matrix.




"""
from ...prompts import format_prompt_for_tables
from ..matrix import co_occurrence_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def item_associations(
    item,
    obj=None,
    #
    # Co-occ matrix params:
    columns=None,
    rows=None,
    #
    # Columns item filters:
    col_top_n=None,
    col_occ_range=None,
    col_gc_range=None,
    col_custom_items=None,
    #
    # Rows item filters :
    row_top_n=None,
    row_occ_range=None,
    row_gc_range=None,
    row_custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes the associations of a item in a co-occurrence matrix."""

    def compute_obj(obj):
        if obj is not None:
            return obj
        return co_occurrence_matrix(
            columns=columns,
            rows=rows,
            #
            # Columns item filters:
            col_top_n=col_top_n,
            col_occ_range=col_occ_range,
            col_gc_range=col_gc_range,
            col_custom_items=col_custom_items,
            #
            # Rows item filters :
            row_top_n=row_top_n,
            row_occ_range=row_occ_range,
            row_gc_range=row_gc_range,
            row_custom_items=row_custom_items,
            #
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    def extract_item_column_from_coc_matrix(obj, pos, name):
        matrix = obj.matrix_.copy()
        series = matrix.iloc[:, pos]
        series = series.drop(labels=[name], axis=0, errors="ignore")
        series = series[series > 0]
        series.index.name = obj.rows_
        return series

    def create_prompt(field, item, table):
        main_text = (
            "Your task is to generate a short analysis of a table for a "
            "research paper. Summarize the table below, delimited by triple "
            "backticks, in one unique paragraph with at most 30 words. The "
            "table contains the values of co-occurrence (OCC) of the "
            f"'{item}' with the '{field}' field in a bibliographic dataset. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the research field. Be sure "
            "to provide a concise summary of your findings."
        )
        table_text = table.to_markdown()
        return format_prompt_for_tables(main_text, table_text)

    #
    # Main code:
    #
    obj = compute_obj(obj)
    pos, name = extract_item_position_and_name(obj.matrix_.columns, item)
    series = extract_item_column_from_coc_matrix(obj, pos, name)
    prompt = create_prompt(obj.rows_, item, series)

    return name, series, pos, prompt
