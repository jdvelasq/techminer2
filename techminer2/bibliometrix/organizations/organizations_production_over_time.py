"""
Organizations' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__organizations_production_over_time.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.organizations_production_over_time(
...    topics_length=10, 
...    directory=directory,
... )

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__organizations_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.documents_per_organization_.head().to_markdown())
|    | organizations                               | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:--------------------------------------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | ---Teichmann International  AG              | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Harvard University                          | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | University of Messina                       | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | Chinese University of Hong Kong             | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | Nottingham University Business School China | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |

>>> print(r.production_per_year_.head().to_markdown())
|                                                                       |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:----------------------------------------------------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('---3PB', 2022)                                                      |     1 |         1 |                  3 |                 1 |     2 |                       1.5   |                      0.5   |
| ('---AML Forensic library KPMG Luxembourg Societe Cooperative', 2020) |     1 |         1 |                 10 |                 3 |     4 |                       2.5   |                      0.75  |
| ('---BITS Pilani', 2020)                                              |     1 |         1 |                  2 |                 3 |     4 |                       0.5   |                      0.75  |
| ('---Centre for Law', 2017)                                           |     1 |         1 |                150 |                 0 |     7 |                      21.429 |                      0     |
| ('---Deloitte LLP', 2018)                                             |     1 |         1 |                  8 |                 5 |     6 |                       1.333 |                      0.833 |


>>> print(r.table_.head().to_markdown())
| organizations                   |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:--------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| University of Hong Kong 3:185   |      2 |      0 |      0 |      1 |      0 |      0 |
| University College Cork 3:041   |      0 |      1 |      1 |      0 |      0 |      1 |
| Ahlia University 3:019          |      0 |      0 |      0 |      1 |      1 |      1 |
| ---FinTech HK 2:161             |      2 |      0 |      0 |      0 |      0 |      0 |
| University of Westminster 2:017 |      0 |      0 |      0 |      1 |      0 |      1 |

>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the organizations. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                             |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:----------------------------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| University of Hong Kong 3:185                             |      2 |      0 |      0 |      1 |      0 |      0 |
| University College Cork 3:041                             |      0 |      1 |      1 |      0 |      0 |      1 |
| Ahlia University 3:019                                    |      0 |      0 |      0 |      1 |      1 |      1 |
| ---FinTech HK 2:161                                       |      2 |      0 |      0 |      0 |      0 |      0 |
| University of Westminster 2:017                           |      0 |      0 |      0 |      1 |      0 |      1 |
| Coventry University 2:017                                 |      0 |      0 |      0 |      1 |      0 |      1 |
| Dublin City University 2:014                              |      0 |      0 |      0 |      1 |      1 |      0 |
| Politecnico di Milano 2:002                               |      0 |      0 |      0 |      1 |      0 |      1 |
| ---School of Electrical Engineering and Informatics 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |
| ---Kingston Business School 1:153                         |      0 |      1 |      0 |      0 |      0 |      0 |
<BLANKLINE>
<BLANKLINE>

"""
from ... import vantagepoint
from ...techminer.indicators.indicators_by_item_per_year import (
    indicators_by_item_per_year,
)
from ..documents_per_criterion import documents_per_criterion


def organizations_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    cumulative=False,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Institution production over time."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        criterion="organizations",
        topics_length=topics_length,
        topic_occ_min=topic_min_occ,
        topic_occ_max=topic_max_occ,
        topic_citations_min=topic_min_citations,
        topic_citations_max=topic_max_citations,
        custom_topics=custom_topics,
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        cummulative=cumulative,
        **filters,
    )

    chart = vantagepoint.report.gantt_chart(
        terms_by_year,
        title="Organizations' production over time",
    )

    chart.documents_per_organization_ = documents_per_criterion(
        criterion="organizations",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.production_per_year_ = indicators_by_item_per_year(
        field="organizations",
        root_dir=directory,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart
