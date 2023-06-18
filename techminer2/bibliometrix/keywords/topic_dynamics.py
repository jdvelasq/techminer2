# flake8: noqa
"""
Topic Dynamics
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__keywords_dynamics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.keywords.topic_dynamics(
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__keywords_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown())
| keywords                     |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_COMPLIANCE 09:034 |      1 |      0 |      1 |      3 |      1 |      2 |      1 |
| COMPLIANCE 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| FINANCE 07:017               |      1 |      0 |      1 |      1 |      1 |      3 |      0 |


>>> print(r.prompt_)
Your task is to generate an analysis about the  occurrences \\
by year of the 'keywords' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research field. Be sure \\
to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| keywords                     |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_COMPLIANCE 09:034 |      1 |      0 |      1 |      3 |      1 |      2 |      1 |
| COMPLIANCE 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| FINANCE 07:017               |      1 |      0 |      1 |      1 |      1 |      3 |      0 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
# from ... import vantagepoint
# from ...techminer.indicators.indicators_by_field_per_year import (
#     indicators_by_field_per_year,
# )
# from ..documents_per_criterion import documents_per_criterion

FIELD = "keywords"


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
