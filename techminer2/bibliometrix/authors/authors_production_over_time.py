# flake8: noqa
"""
Authors' Production over Time
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__authors_production_over_time.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.authors_production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> print(r.documents_per_item_.head().to_markdown())
|    | authors     | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Teichmann F | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Boticiu SR  | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | Sergi BS    | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | Lan G       | costs of voting and firm PERFORMANCE: evidence from REGTECH adoption in chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | Li D/1      | costs of voting and firm PERFORMANCE: evidence from REGTECH adoption in chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |


>>> print(r.production_per_year_.head().to_markdown())
|                             |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:----------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('Abdullah Y', 2022)        |     1 |         1 |                  1 |                 0 |     2 |                       0.5   |                      0     |
| ('Ajmi JA', 2021)           |     1 |         1 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('Anagnostopoulos I', 2018) |     1 |         1 |                153 |                17 |     6 |                      25.5   |                      2.833 |
| ('Anasweh M', 2020)         |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| ('Arman AA', 2022)          |     2 |         2 |                  0 |                 0 |     2 |                       0     |                      0     |



>>> print(r.table_.head().to_markdown())
| authors           |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185    |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Buckley RP 3:185  |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Barberis JN 2:161 |      0 |      2 |      0 |      0 |      0 |      0 |      0 |      0 |
| Butler T/1 2:041  |      0 |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
| Hamdan A 2:018    |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |


>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors           |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185    |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Buckley RP 3:185  |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Barberis JN 2:161 |      0 |      2 |      0 |      0 |      0 |      0 |      0 |      0 |
| Butler T/1 2:041  |      0 |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
| Hamdan A 2:018    |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Turki M 2:018     |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Lin W 2:017       |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Singh C 2:017     |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Brennan R 2:014   |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Crane M 2:014     |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ...classes import ProductionOverTimeChart
from ...techminer.indicators.indicators_by_field_per_year import (
    indicators_by_field_per_year,
)
from ...vantagepoint.analyze import terms_by_year
from ...vantagepoint.report import gantt_chart
from ..documents_per_criterion import documents_per_criterion


def authors_production_over_time(
    root_dir="./",
    database="main",
    # Table params:
    cumulative=False,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Authors production over time."""

    items_by_year = terms_by_year(
        field="authors",
        root_dir=root_dir,
        database=database,
        # Table params:
        cumulative=cumulative,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    chart = gantt_chart(
        items_by_year,
        title="Authors' production over time",
    )

    obj = ProductionOverTimeChart()
    obj.plot_ = chart.plot_
    obj.table_ = items_by_year.table_.copy()
    obj.prompt_ = chart.prompt_

    obj.documents_per_item_ = documents_per_criterion(
        field="authors",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj.production_per_year_ = indicators_by_field_per_year(
        field="authors",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return obj
