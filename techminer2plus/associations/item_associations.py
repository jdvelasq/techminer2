"""Computes the associations of a item in a co-occurrence matrix.




"""
# from ...chatbot_prompts import format_chatbot_prompt_for_tables
# from ..matrix import co_occurrence_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def item_associations(
    item,
    cooc_matrix=None,
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
        return format_chatbot_prompt_for_tables(main_text, table_text)

    #
    # Main code:
    #
    pos, name = extract_item_position_and_name(
        cooc_matrix.matrix_.columns, item
    )
    series = extract_item_column_from_coc_matrix(cooc_matrix, pos, name)
    prompt = create_prompt(cooc_matrix.rows_, item, series)

    return name, series, pos, prompt
