"""
Sources' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__sources_production_over_time.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.sources_production_over_time(
...    topics_length=10,
...    directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__sources_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.documents_per_source_.head().to_markdown())
|    | source_abbr        | title                                                                                               |   year | source_title                                   |   global_citations |   local_citations | doi                            |
|---:|:-------------------|:----------------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:-------------------------------|
|  0 | TECHNOL SOC        | RegTech  Potential benefits and challenges for businesses                                           |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150  |
|  1 | RES INT BUS FINANC | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms        |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868    |
|  2 | COMPUTER           | RegTech's Rise                                                                                      |   2022 | Computer                                       |                  0 |                 0 | 10.1109/MC.2022.3176693        |
|  3 | FIN INNOV          | Fintech, regtech, and financial development: evidence from China                                    |   2022 | Financial Innovation                           |                 13 |                 1 | 10.1186/S40854-021-00313-6     |
|  4 | J CORP FINANC      | Too much to learn? The (un)intended consequences of RegTech development on mergers and acquisitions |   2022 | Journal of Corporate Finance                   |                  0 |                 0 | 10.1016/J.JCORPFIN.2022.102276 |


>>> print(r.production_per_year_.head().to_markdown())
|                                 |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:--------------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('ACM INT CONF PROC SER', 2021) |     1 |         1 |                  2 |                 0 |     3 |                       0.667 |                      0     |
| ('ADELAIDE LAW REV', 2020)      |     1 |         1 |                  5 |                 1 |     4 |                       1.25  |                      0.25  |
| ('ADV INTELL SYS COMPUT', 2021) |     1 |         1 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('CEUR WKSHP PROC', 2020)       |     1 |         1 |                  2 |                 3 |     4 |                       0.5   |                      0.75  |
| ('COMPUTER', 2022)              |     1 |         1 |                  0 |                 0 |     2 |                       0     |                      0     |


>>> print(r.table_.to_markdown())
| source_abbr                         |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| J BANK REGUL 2:035                  |      0 |      0 |      0 |      0 |      1 |      1 |      0 |
| J FINANC CRIME 2:013                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |
| FOSTER INNOV AND COMPET WITH 2:001  |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| STUD COMPUT INTELL 2:001            |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| ROUTLEDGE HANDB OF FIN TECHNO 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| INT CONF INF TECHNOL SYST INN 2:000 |      0 |      0 |      0 |      0 |      0 |      0 |      2 |
| J ECON BUS 1:153                    |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| NORTHWEST J INTL LAW BUS 1:150      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| PALGRAVE STUD DIGIT BUS ENABL 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
| DUKE LAW J 1:030                    |      1 |      0 |      0 |      0 |      0 |      0 |      0 |


>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the source_abbr. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                         |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| J BANK REGUL 2:035                  |      0 |      0 |      0 |      0 |      1 |      1 |      0 |
| J FINANC CRIME 2:013                |      0 |      0 |      0 |      0 |      1 |      0 |      1 |
| FOSTER INNOV AND COMPET WITH 2:001  |      0 |      0 |      0 |      0 |      2 |      0 |      0 |
| STUD COMPUT INTELL 2:001            |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| ROUTLEDGE HANDB OF FIN TECHNO 2:000 |      0 |      0 |      0 |      0 |      0 |      2 |      0 |
| INT CONF INF TECHNOL SYST INN 2:000 |      0 |      0 |      0 |      0 |      0 |      0 |      2 |
| J ECON BUS 1:153                    |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
| NORTHWEST J INTL LAW BUS 1:150      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
| PALGRAVE STUD DIGIT BUS ENABL 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
| DUKE LAW J 1:030                    |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
<BLANKLINE>
<BLANKLINE>

"""
from ... import vantagepoint
from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from ..documents_per_criterion import documents_per_criterion


def sources_production_over_time(
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
    """Sources production over time."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        criterion="source_abbr",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        cumulative=cumulative,
        **filters,
    )

    chart = vantagepoint.report.gantt_chart(
        terms_by_year,
        title="Sources' production over time",
    )

    chart.documents_per_source_ = documents_per_criterion(
        criterion="source_abbr",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.production_per_year_ = indicators_by_topic_per_year(
        criterion="source_abbr",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart
