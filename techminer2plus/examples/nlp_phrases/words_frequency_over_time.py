# flake8: noqa
"""
Word Frequency over Time
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/nlp_phrases/words_frequency_over_time.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.nlp_phrases.words_frequency_over_time(
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/nlp_phrases/words_frequency_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.table_.head().to_markdown())
| nlp_phrases                   |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_TECHNOLOGY 18:273  |      0 |      2 |      0 |      2 |      6 |      3 |      5 |      0 |
| FINANCIAL_INSTITUTIONS 15:194 |      0 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| FINANCIAL_REGULATION 07:360   |      1 |      1 |      1 |      1 |      0 |      2 |      1 |      0 |
| REGULATORY_COMPLIANCE 07:198  |      0 |      0 |      2 |      1 |      2 |      1 |      1 |      0 |
| FINANCIAL_SECTOR 07:169       |      0 |      1 |      0 |      0 |      1 |      3 |      2 |      0 |



>>> print(r.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'nlp_phrases' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| nlp_phrases                   |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_TECHNOLOGY 18:273  |      0 |      2 |      0 |      2 |      6 |      3 |      5 |      0 |
| FINANCIAL_INSTITUTIONS 15:194 |      0 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| FINANCIAL_REGULATION 07:360   |      1 |      1 |      1 |      1 |      0 |      2 |      1 |      0 |
| REGULATORY_COMPLIANCE 07:198  |      0 |      0 |      2 |      1 |      2 |      1 |      1 |      0 |
| FINANCIAL_SECTOR 07:169       |      0 |      1 |      0 |      0 |      1 |      3 |      2 |      0 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...analyze import terms_by_year as analyze_terms_by_year
from ...query import indicators_by_field_per_year
from ...visualize import gantt_chart
from ..documents_per_criterion import documents_per_criterion

FIELD = "nlp_phrases"


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
