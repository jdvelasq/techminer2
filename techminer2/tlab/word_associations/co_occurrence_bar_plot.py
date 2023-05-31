# flake8: noqa
"""
Co-occurrences Bar Plot --- ChatGPT
===============================================================================

Plots the co-occurrences of a given descriptor with the remaining descriptors.



Example:
-------------------------------------------------------------------------------

>>> # Step 1: Import the VantagePoint module.
>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> #
>>> # Step 2: Create a co-occurrence matrix
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> #
>>> # Step 3: Create a subset of the co-occurrence matrix with the term to be
>>> # analyzed.
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    topics='regtech',
... )
>>> # Step 4: Visualize the co-occurrences as a bar plot.
>>> from techminer2 import tlab
>>> file_name = "sphinx/_static/tlab__word_associations__co_occurrences_bar_plot.html"
>>> chart = tlab.word_associations.co_occurrence_bar_plot(matrix_subset)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations__co_occurrences_bar_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>
 
    
>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence(OCC) of the \
'regtech' with the 'author_keywords' field in a bibliographic dataset. \
Identify any notable patterns, trends, or outliers in the data, and discuss \
their implications for the research field. Be sure to provide a concise \
summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   OCC |
|:-------------------------------|------:|
| fintech 12:249                 |    12 |
| compliance 07:030              |     7 |
| regulation 05:164              |     4 |
| financial services 04:168      |     3 |
| suptech 03:004                 |     3 |
| regulatory technology 07:037   |     2 |
| financial regulation 04:035    |     2 |
| artificial intelligence 04:023 |     2 |
| risk management 03:014         |     2 |
| blockchain 03:005              |     2 |
| anti-money laundering 03:021   |     1 |
| innovation 03:012              |     1 |

"""

from ...classes import ListView
from ...vantagepoint.report import bar_chart


def co_occurrence_bar_plot(
    obj,
    title=None,
    criterion_label=None,
    metric_label=None,
):
    """Co-occurrence bar plot"""

    def create_chatgpt_prompt(criterion, term, table):
        return (
            "Analyze the table below which contains values of co-occurrence"
            f"(OCC) of the '{term}' with the '{criterion}' field in a "
            "bibliographic dataset. Identify any notable patterns, trends, "
            "or outliers in the data, and discuss their implications for "
            "the research field. Be sure to provide a concise summary of "
            "your findings in no more than 150 words."
            f"\n\n{table.to_markdown()}"
        )

    #
    # Main:
    #
    term = " ".join(obj.topics_[0].split(" ")[:-1])

    if title is None:
        title = f"Co-occurrence with '{term}'"

    list_view = ListView()
    list_view.table_ = obj.matrix_.copy()
    list_view.table_.columns = ["OCC"]
    list_view.table_ = list_view.table_.sort_values("OCC", ascending=False)
    list_view.metric_ = "OCC"
    list_view.criterion_ = obj.criterion_
    list_view.prompt_ = obj.prompt_

    chart = bar_chart(
        list_view,
        title=title,
        field_label=criterion_label,
        metric_label=metric_label,
    )

    chart.prompt_ = create_chatgpt_prompt(
        list_view.criterion_, term, list_view.table_
    )

    return chart
