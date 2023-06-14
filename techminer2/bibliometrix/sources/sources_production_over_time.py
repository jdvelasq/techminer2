# flake8: noqa
"""
Sources' Production over Time
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__sources_production_over_time.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.sources_production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__sources_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.documents_per_item_.head().to_markdown())
|    | source_abbr        | title                                                                                               |   year | source_title                                   |   global_citations |   local_citations | doi                            |
|---:|:-------------------|:----------------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:-------------------------------|
|  0 | TECHNOL SOC        | REGTECH POTENTIAL_BENEFITS and CHALLENGES for businesses                                            |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150  |
|  1 | RES INT BUS FINANC | COSTS_OF_VOTING and FIRM_PERFORMANCE: evidence from REGTECH ADOPTION in chinese listed firms        |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868    |
|  2 | COMPUTER           | REGTECH's rise                                                                                      |   2022 | Computer                                       |                  0 |                 0 | 10.1109/MC.2022.3176693        |
|  3 | FINANCIAL INNOV    | FINTECH, REGTECH, and FINANCIAL_DEVELOPMENT: evidence from CHINA                                    |   2022 | Financial Innovation                           |                 13 |                 1 | 10.1186/S40854-021-00313-6     |
|  4 | J CORP FINANC      | too much to learn? the (un)intended consequences of REGTECH DEVELOPMENT on MERGERS_AND_ACQUISITIONS |   2022 | Journal of Corporate Finance                   |                  0 |                 0 | 10.1016/J.JCORPFIN.2022.102276 |




>>> print(r.production_per_year_.head().to_markdown())
|                                 |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:--------------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('ACM INT CONF PROC SER', 2021) |     1 |         1 |                  2 |                 0 |     3 |                       0.667 |                      0     |
| ('ADELAIDE LAW REV', 2020)      |     1 |         1 |                  5 |                 1 |     4 |                       1.25  |                      0.25  |
| ('ADV INTELL SYS COMPUT', 2021) |     1 |         1 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('CEUR WORKSHOP PROC', 2020)    |     1 |         1 |                  2 |                 3 |     4 |                       0.5   |                      0.75  |
| ('COMPUTER', 2022)              |     1 |         1 |                  0 |                 0 |     2 |                       0     |                      0     |




>>> print(r.table_.to_markdown())
| source_abbr                         |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| J BANK REGUL 2:035                  |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| J FINANC CRIME 2:013                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| FOSTER INNOVCOMPET WITH FINTE 2:001 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |      0 |
| STUD COMPUT INTELL 2:001            |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| INT CONF INF TECHNOL SYST INN 2:000 |      0 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| ROUTLEDGE HANDBFINANCIAL TECH 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| J ECON BUS 1:153                    |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| NORTHWEST J INTL LAW BUS 1:150      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| PALGRAVE STUD DIGIT BUS ENABL 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| DUKE LAW J 1:030                    |      1 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |



>>> print(r.prompt_)
Your task is to generate an analysis about the  occurrences \\
by year of the 'source_abbr' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research field. Be sure \\
to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                         |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| J BANK REGUL 2:035                  |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| J FINANC CRIME 2:013                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| FOSTER INNOVCOMPET WITH FINTE 2:001 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |      0 |
| STUD COMPUT INTELL 2:001            |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| INT CONF INF TECHNOL SYST INN 2:000 |      0 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| ROUTLEDGE HANDBFINANCIAL TECH 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| J ECON BUS 1:153                    |      0 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| NORTHWEST J INTL LAW BUS 1:150      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| PALGRAVE STUD DIGIT BUS ENABL 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| DUKE LAW J 1:030                    |      1 |      0 |      0 |      0 |      0 |      0 |      0 |      0 |
```
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


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def sources_production_over_time(
    # Table params:
    cumulative=False,
    # Item filters:
    top_n=50,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Sources production over time."""

    items_by_year = terms_by_year(
        field="source_abbr",
        # Table params:
        cumulative=cumulative,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    chart = gantt_chart(
        items_by_year,
        title="Sources' Production over Time",
    )

    obj = ProductionOverTimeChart()
    obj.plot_ = chart.plot_
    obj.table_ = items_by_year.table_.copy()
    obj.prompt_ = chart.prompt_

    obj.documents_per_item_ = documents_per_criterion(
        field="source_abbr",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj.production_per_year_ = indicators_by_field_per_year(
        field="source_abbr",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return obj
