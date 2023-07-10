# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _item_associations_prompt:

Item Associations Prompt
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.item_associations_prompt(
...    item='REGTECH',
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate a short analysis of a table for a research paper. \\
Summarize the table below, delimited by triple backticks, in one unique \\
paragraph with at most 30 words. The table contains the values of co- \\
occurrence (OCC) of the 'REGTECH' with the 'author_keywords' field in a \\
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


"""
from .format_prompt_for_dataframes import format_prompt_for_dataframes
from .item_associations_table import item_associations_table


def item_associations_prompt(
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

    data_frame = item_associations_table(
        #
        # FUNCTION PARAMS:
        item=item,
        #
        # CO-OCC PARAMS:
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

    main_text = (
        "Your task is to generate a short analysis of a table for a "
        "research paper. Summarize the table below, delimited by triple "
        "backticks, in one unique paragraph with at most 30 words. The "
        "table contains the values of co-occurrence (OCC) of the "
        f"'{item}' with the '{columns}' field in a bibliographic dataset. "
        "Identify any notable patterns, trends, or outliers in the data, "
        "and discuss their implications for the research field. Be sure "
        "to provide a concise summary of your findings."
    )
    table_text = data_frame.to_markdown()
    return format_prompt_for_dataframes(main_text, table_text)
