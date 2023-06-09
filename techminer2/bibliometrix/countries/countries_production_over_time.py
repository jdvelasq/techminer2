# flake8: noqa
"""
Countries' Production over Time
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__countries_production_over_time.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.countries_production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.documents_per_item_.head().to_markdown())
|    | countries     | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:--------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Italy         | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Switzerland   | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | United States | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | China         | costs of voting and firm PERFORMANCE: evidence from REGTECH adoption in chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | United States | REGTECH's rise                                                                               |   2022 | Computer                                       |                  0 |                 0 | 10.1109/MC.2022.3176693       |

>>> print(r.production_per_year_.head().to_markdown())
|                     |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:--------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('Australia', 2017) |     2 |         2 |                161 |                 3 |     7 |                      23     |                      0.429 |
| ('Australia', 2020) |     3 |         5 |                 33 |                 9 |     4 |                       8.25  |                      2.25  |
| ('Australia', 2021) |     2 |         7 |                  5 |                 3 |     3 |                       1.667 |                      1     |
| ('Bahrain', 2020)   |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| ('Bahrain', 2021)   |     2 |         3 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |



>>> print(r.table_.head().to_markdown())
| countries            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| United Kingdom 7:199 |      0 |      0 |      3 |      1 |      2 |      0 |      1 |      0 |
| Australia 7:199      |      0 |      2 |      0 |      0 |      3 |      2 |      0 |      0 |
| United States 6:059  |      1 |      0 |      1 |      2 |      0 |      0 |      1 |      1 |
| Ireland 5:055        |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      0 |
| China 5:027          |      0 |      1 |      0 |      0 |      0 |      0 |      3 |      1 |


>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| United Kingdom 7:199 |      0 |      0 |      3 |      1 |      2 |      0 |      1 |      0 |
| Australia 7:199      |      0 |      2 |      0 |      0 |      3 |      2 |      0 |      0 |
| United States 6:059  |      1 |      0 |      1 |      2 |      0 |      0 |      1 |      1 |
| Ireland 5:055        |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      0 |
| China 5:027          |      0 |      1 |      0 |      0 |      0 |      0 |      3 |      1 |
| Italy 5:005          |      0 |      0 |      0 |      1 |      1 |      1 |      1 |      1 |
| Germany 4:051        |      0 |      0 |      1 |      0 |      2 |      0 |      1 |      0 |
| Switzerland 4:045    |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      1 |
| Bahrain 4:019        |      0 |      0 |      0 |      0 |      1 |      2 |      1 |      0 |
| Hong Kong 3:185      |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
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


def countries_production_over_time(
    root_dir="./",
    database="main",
    # Table params:
    cumulative=False,
    # Item filters:
    top_n=50,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Country production over time."""

    items_by_year = terms_by_year(
        field="countries",
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
        title="Contry' production over time",
    )

    obj = ProductionOverTimeChart()
    obj.plot_ = chart.plot_
    obj.table_ = items_by_year.table_.copy()
    obj.prompt_ = chart.prompt_

    obj.documents_per_item_ = documents_per_criterion(
        field="countries",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj.production_per_year_ = indicators_by_field_per_year(
        field="countries",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return obj
