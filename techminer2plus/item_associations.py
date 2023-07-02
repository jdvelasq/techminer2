# flake8: noqa
"""
.. _item_associations:

Item Associations
===============================================================================

Computes the associations of a item in a co-occurrence matrix.

>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> associations = techminer2plus.item_associations("REGTECH", cooc_matrix)
>>> associations.df_
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


>>> print(associations.prompt_)
Your task is to generate a short analysis of a table for a research paper. \\
Summarize the table below, delimited by triple backticks, in one unique \\
paragraph with at most 30 words. The table contains the values of co- \\
occurrence (OCC) of the 'author_keywords' with the 'REGTECH' field in a \\
bibliographic dataset. Identify any notable patterns, trends, or outliers \\
in the data, and discuss their implications for the research field. Be sure \\
to provide a concise summary of your findings.
<BLANKLINE>
Table:
```
| author_keywords                |   REGTECH 28:329 |
|:-------------------------------|-----------------:|
| FINTECH 12:249                 |               12 |
| COMPLIANCE 07:030              |                7 |
| REGULATION 05:164              |                4 |
| FINANCIAL_SERVICES 04:168      |                3 |
| SUPTECH 03:004                 |                3 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |
| FINANCIAL_REGULATION 04:035    |                2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |
| RISK_MANAGEMENT 03:014         |                2 |
| BLOCKCHAIN 03:005              |                2 |
| SEMANTIC_TECHNOLOGIES 02:041   |                2 |
| DATA_PROTECTION 02:027         |                2 |
| SMART_CONTRACTS 02:022         |                2 |
| CHARITYTECH 02:017             |                2 |
| ENGLISH_LAW 02:017             |                2 |
| ACCOUNTABILITY 02:014          |                2 |
| DATA_PROTECTION_OFFICER 02:014 |                2 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |
| INNOVATION 03:012              |                1 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import pandas as pd

from ._chatbot_prompts import format_chatbot_prompt_for_df


@dataclass
class ItemAssociations:
    """Item associations."""

    df_: pd.DataFrame
    item_: str
    metric_: str
    field_: str
    prompt_: str
    item_name_: str


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
        matrix = obj.df_.copy()
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
        return format_chatbot_prompt_for_df(main_text, table_text)

    #
    # Main code:
    #
    pos, name = extract_item_position_and_name(cooc_matrix.df_.columns, item)
    series = extract_item_column_from_coc_matrix(cooc_matrix, pos, name)
    frame = series.to_frame()
    frame["OCC"] = [text.split(" ")[-1].split(":")[0] for text in frame.index]
    frame["GC"] = [text.split(" ")[-1].split(":")[-1] for text in frame.index]
    frame["NAME"] = [" ".join(text.split(" ")[:-1]) for text in frame.index]
    frame = frame.sort_values(
        by=[name, "OCC", "GC", "NAME"], ascending=[False, False, False, True]
    )
    series = frame[name]
    prompt = create_prompt(item, cooc_matrix.rows_, series)

    return ItemAssociations(
        df_=series.to_frame(),
        item_=item,
        metric_="OCC",
        field_=cooc_matrix.rows_,
        prompt_=prompt,
        item_name_=name,
    )
