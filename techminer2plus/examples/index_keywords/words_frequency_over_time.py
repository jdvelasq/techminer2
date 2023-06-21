# flake8: noqa
"""
Word Frequency over Time
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/index_keywords/words_frequency_over_time.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.index_keywords.words_frequency_over_time(
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/index_keywords/words_frequency_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown())
| index_keywords              |   2017 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_COMPLIANCE 9:34  |      1 |      1 |      3 |      1 |      2 |      1 |
| FINANCIAL_INSTITUTIONS 6:09 |      0 |      0 |      3 |      1 |      2 |      0 |
| FINANCE 5:16                |      1 |      1 |      0 |      1 |      2 |      0 |
| REGTECH 5:15                |      2 |      1 |      0 |      0 |      2 |      0 |
| ANTI_MONEY_LAUNDERING 3:10  |      0 |      0 |      1 |      2 |      0 |      0 |


>>> print(r.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'index_keywords' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| index_keywords              |   2017 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_COMPLIANCE 9:34  |      1 |      1 |      3 |      1 |      2 |      1 |
| FINANCIAL_INSTITUTIONS 6:09 |      0 |      0 |      3 |      1 |      2 |      0 |
| FINANCE 5:16                |      1 |      1 |      0 |      1 |      2 |      0 |
| REGTECH 5:15                |      2 |      1 |      0 |      0 |      2 |      0 |
| ANTI_MONEY_LAUNDERING 3:10  |      0 |      0 |      1 |      2 |      0 |      0 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...analyze import terms_by_year as analyze_terms_by_year
from ...query import indicators_by_field_per_year
from ...visualize import gantt_chart
from ..documents_per_criterion import documents_per_criterion

FIELD = "index_keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def words_frequency_over_time(
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

    terms_by_year = analyze_terms_by_year(
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

    chart = gantt_chart(
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
