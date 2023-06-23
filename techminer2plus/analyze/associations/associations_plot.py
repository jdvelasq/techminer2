# flake8: noqa
"""
Associations Plot
===============================================================================

Plots the co-occurrences of a given descriptor with the remaining descriptors.




>>> ROOT_DIR = "data/regtech/"
>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=ROOT_DIR,
... )
>>> file_name = "sphinx/_static/analyze/associations/associations_plot.html"
>>> chart = techminer2plus.analyze.associations.associations_plot(item="REGTECH", cooc_matrix=cooc_matrix)
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
| author_keywords                |   REGTECH 28:329 |
|:-------------------------------|-----------------:|
| FINTECH 12:249                 |               12 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |
| COMPLIANCE 07:030              |                7 |
| REGULATION 05:164              |                4 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |
| FINANCIAL_SERVICES 04:168      |                3 |
| FINANCIAL_REGULATION 04:035    |                2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |
| RISK_MANAGEMENT 03:014         |                2 |
| INNOVATION 03:012              |                1 |
| BLOCKCHAIN 03:005              |                2 |
| SUPTECH 03:004                 |                3 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""

from ...classes import ItemsList
from ...report import ranking_chart
from .item_associations import item_associations


def associations_plot(
    item,
    cooc_matrix,
    title=None,
    field_label=None,
    metric_label=None,
):
    """association plot"""

    #
    # Main:
    #
    _, series, _, prompt = item_associations(
        item=item,
        cooc_matrix=cooc_matrix,
    )

    if title is None:
        title = f"Co-occurrence with '{item}'"

    frame = series.to_frame()
    frame.columns = ["OCC"]
    frame = frame.sort_values("OCC", ascending=False)

    list_view = ItemsList()
    list_view.table_ = frame
    list_view.metric_ = "OCC"
    list_view.field_ = cooc_matrix.rows_
    list_view.prompt_ = prompt

    chart = ranking_chart(
        list_view,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
    )

    chart.prompt_ = prompt

    return chart
