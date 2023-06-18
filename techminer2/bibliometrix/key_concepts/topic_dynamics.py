# flake8: noqa
"""
Topic Dynamics
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__key_concepts_dynamics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.key_concepts.topic_dynamics(
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__key_concepts_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown())
| key_concepts                  |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                |      0 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| REGULATORY_TECHNOLOGY 20:274  |      0 |      2 |      0 |      2 |      6 |      4 |      5 |      1 |
| REGULATORY_COMPLIANCE 15:232  |      0 |      1 |      2 |      2 |      5 |      2 |      2 |      1 |
| FINANCIAL_INSTITUTIONS 15:194 |      0 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| FINANCIAL_REGULATION 12:395   |      1 |      2 |      1 |      1 |      1 |      2 |      4 |      0 |


>>> print(r.prompt_)
Your task is to generate an analysis about the  occurrences \\
by year of the 'key_concepts' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research field. Be sure \\
to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| key_concepts                  |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                |      0 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| REGULATORY_TECHNOLOGY 20:274  |      0 |      2 |      0 |      2 |      6 |      4 |      5 |      1 |
| REGULATORY_COMPLIANCE 15:232  |      0 |      1 |      2 |      2 |      5 |      2 |      2 |      1 |
| FINANCIAL_INSTITUTIONS 15:194 |      0 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| FINANCIAL_REGULATION 12:395   |      1 |      2 |      1 |      1 |      1 |      2 |      4 |      0 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
# from ... import vantagepoint
# from ...techminer.indicators.indicators_by_field_per_year import (
#     indicators_by_field_per_year,
# )
# from ..documents_per_criterion import documents_per_criterion

FIELD = "key_concepts"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def topic_dynamics(
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    cumulative=False,
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Makes a dynamics chat for top words."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        field=FIELD,
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

    chart = vantagepoint.charts.gantt_chart(
        terms_by_year,
        title=FIELD.replace("_", " ").title() + " Dynamics",
    )

    chart.documents_per_keyword_ = documents_per_criterion(
        field=FIELD,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    chart.production_per_year_ = indicators_by_field_per_year(
        field=FIELD,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart
