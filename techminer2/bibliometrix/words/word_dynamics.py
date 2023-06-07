# flake8: noqa
"""
Word Dynamics
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__word_dynamics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.words.word_dynamics(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__word_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown())
| author_keywords           |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:--------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329            |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249            |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| COMPLIANCE 07:030         |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164         |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| FINANCIAL_SERVICES 04:168 |      1 |      1 |      0 |      1 |      0 |      1 |      0 |



>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords           |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:--------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329            |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249            |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| COMPLIANCE 07:030         |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164         |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| FINANCIAL_SERVICES 04:168 |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ... import vantagepoint
from ...techminer.indicators.indicators_by_item_per_year import (
    indicators_by_item_per_year,
)
from ..documents_per_criterion import documents_per_criterion


def word_dynamics(
    field="author_keywords",
    top_n=50,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    cumulative=False,
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Makes a dynamics chat for top words."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        field=field,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        cumulative=cumulative,
        **filters,
    )

    chart = vantagepoint.report.gantt_chart(
        terms_by_year,
        title=field.replace("_", " ").title() + " Dynamics",
    )

    chart.documents_per_keyword_ = documents_per_criterion(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    chart.production_per_year_ = indicators_by_item_per_year(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart


def _create_prompt(table, criterion):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on cumulative occurrences of {criterion.replace("_", " ")} \
for the top {table.shape[0]} most frequent {criterion.replace("_", " ")} in the dataset. \
Use the information in the table to draw conclusions about the cumulative \
occurrence per year of the {criterion.replace("_", " ")}. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
