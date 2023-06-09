# flake8: noqa
"""
Organizations' Production over Time
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__organizations_production_over_time.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.organizations_production_over_time(
...    top_n=10, 
...    root_dir=root_dir,
... )

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__organizations_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.documents_per_item_.head().to_markdown())
|    | organizations                              | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:-------------------------------------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Harvard Univ (USA)                         | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Teichmann International (Schweiz) AG (CHE) | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | Univ of Messina (ITA)                      | REGTECH  POTENTIAL_BENEFITS and CHALLENGES for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | Nottingham Univ Bus Sch China (CHN)        | costs of voting and firm PERFORMANCE: evidence from REGTECH adoption in chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | Shenzhen Univ (CHN)                        | costs of voting and firm PERFORMANCE: evidence from REGTECH adoption in chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |




>>> print(r.production_per_year_.head().to_markdown())
|                                                                                                  |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:-------------------------------------------------------------------------------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('3PB, London, United Kingdom (GBR)', 2022)                                                      |     1 |         1 |                  3 |                 1 |     2 |                       1.5   |                      0.5   |
| ('AML Forensic library KPMG Luxembourg Societe Cooperative, Luxembourg, Luxembourg (LUX)', 2020) |     1 |         1 |                 10 |                 3 |     4 |                       2.5   |                      0.75  |
| ('Ahlia Univ (BHR)', 2020)                                                                       |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| ('Ahlia Univ (BHR)', 2021)                                                                       |     1 |         2 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('Ahlia Univ (BHR)', 2022)                                                                       |     1 |         3 |                  1 |                 0 |     2 |                       0.5   |                      0     |



>>> print(r.table_.head().to_markdown())
| organizations                   |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:--------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Univ of Hong Kong (HKG) 3:185   |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Univ Coll Cork (IRL) 3:041      |      0 |      0 |      1 |      1 |      0 |      0 |      1 |      0 |
| Ahlia Univ (BHR) 3:019          |      0 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| Coventry Univ (GBR) 2:017       |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Univ of Westminster (GBR) 2:017 |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |


>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------------------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Univ of Hong Kong (HKG) 3:185                                            |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Univ Coll Cork (IRL) 3:041                                               |      0 |      0 |      1 |      1 |      0 |      0 |      1 |      0 |
| Ahlia Univ (BHR) 3:019                                                   |      0 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| Coventry Univ (GBR) 2:017                                                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Univ of Westminster (GBR) 2:017                                          |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Dublin City Univ (IRL) 2:014                                             |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| Politec di Milano (ITA) 2:002                                            |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| Kingston Bus Sch (GBR) 1:153                                             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| FinTech HK, Hong Kong (HKG) 1:150                                        |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
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


def organizations_production_over_time(
    root_dir="./",
    database="documents",
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
    """Institution production over time."""

    items_by_year = terms_by_year(
        field="organizations",
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
        title="Organizations' production over time",
    )

    obj = ProductionOverTimeChart()
    obj.plot_ = chart.plot_
    obj.table_ = items_by_year.table_.copy()
    obj.prompt_ = chart.prompt_

    obj.documents_per_item_ = documents_per_criterion(
        field="organizations",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj.production_per_year_ = indicators_by_field_per_year(
        field="organizations",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return obj
