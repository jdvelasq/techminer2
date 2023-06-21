# flake8: noqa
"""
Associations Plot
===============================================================================

Plots the co-occurrences of a given descriptor with the remaining descriptors.




>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> co_occ_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/analyze/associations/associations_plot.html"
>>> chart = techminer2plus.analyze.associations.associations_plot(co_occ_matrix, term="REGTECH")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/analyze/associations/associations_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>
 
    
>>> print(chart.prompt_)
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
| row                            |   OCC |
|:-------------------------------|------:|
| REGTECH 28:329                 |    28 |
| FINTECH 12:249                 |    12 |
| COMPLIANCE 07:030              |     7 |
| REGULATION 05:164              |     4 |
| FINANCIAL_SERVICES 04:168      |     3 |
| SUPTECH 03:004                 |     3 |
| REGULATORY_TECHNOLOGY 07:037   |     2 |
| FINANCIAL_REGULATION 04:035    |     2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |     2 |
| RISK_MANAGEMENT 03:014         |     2 |
| BLOCKCHAIN 03:005              |     2 |
| ANTI_MONEY_LAUNDERING 05:034   |     1 |
| INNOVATION 03:012              |     1 |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""

from ...classes import ItemsList
from ...prompts import format_prompt_for_tables
from ...report import ranking_chart
from ..matrix import co_occurrence_matrix


def associations_plot(
    obj,
    #
    # Function params:
    term=None,
    title=None,
    field_label=None,
    metric_label=None,
    #
    # Co-occurrence matrix params:
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
    """association plot"""

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
    # Main:
    #
    if obj is None:
        obj = co_occurrence_matrix(
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

    if title is None:
        title = f"Co-occurrence with '{term}'"

    data = obj.matrix_.copy()
    data.columns = data.columns.map(lambda w: " ".join(w.split(" ")[:-1]))
    data = data.loc[:, [term]]
    data.columns = ["OCC"]
    data = data[data.OCC > 0]
    data = data.sort_values("OCC", ascending=False)

    list_view = ItemsList()
    list_view.table_ = data
    list_view.metric_ = "OCC"
    list_view.field_ = obj.columns_
    list_view.prompt_ = ""

    chart = ranking_chart(
        list_view,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
    )

    chart.prompt_ = create_prompt(list_view.field_, term, list_view.table_)

    return chart
