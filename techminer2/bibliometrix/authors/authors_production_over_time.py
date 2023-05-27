"""
Authors' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__authors_production_over_time.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.authors_production_over_time(
...    topics_length=10,
...    directory=directory,
... )

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> print(r.documents_per_author_.head().to_markdown())
|    | authors     | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Teichmann F | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Boticiu SR  | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | Sergi BS    | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | Lan G       | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | Li D/1      | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |



>>> print(r.production_per_year_.head().to_markdown())
|                             |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:----------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('Abdullah Y', 2022)        |     1 |         1 |                  1 |                 0 |     2 |                       0.5   |                      0     |
| ('Ajmi JA', 2021)           |     1 |         1 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('Anagnostopoulos I', 2018) |     1 |         1 |                153 |                17 |     6 |                      25.5   |                      2.833 |
| ('Anasweh M', 2020)         |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| ('Arman AA', 2022)          |     2 |         2 |                  0 |                 0 |     2 |                       0     |                      0     |



>>> print(r.table_.head().to_markdown())
| authors           |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185    |      2 |      0 |      0 |      1 |      0 |      0 |
| Buckley RP 3:185  |      2 |      0 |      0 |      1 |      0 |      0 |
| Barberis JN 2:161 |      2 |      0 |      0 |      0 |      0 |      0 |
| Butler T/1 2:041  |      0 |      1 |      1 |      0 |      0 |      0 |
| Hamdan A 2:018    |      0 |      0 |      0 |      1 |      1 |      0 |



>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the authors. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors           |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185    |      2 |      0 |      0 |      1 |      0 |      0 |
| Buckley RP 3:185  |      2 |      0 |      0 |      1 |      0 |      0 |
| Barberis JN 2:161 |      2 |      0 |      0 |      0 |      0 |      0 |
| Butler T/1 2:041  |      0 |      1 |      1 |      0 |      0 |      0 |
| Hamdan A 2:018    |      0 |      0 |      0 |      1 |      1 |      0 |
| Turki M 2:018     |      0 |      0 |      0 |      1 |      1 |      0 |
| Lin W 2:017       |      0 |      0 |      0 |      1 |      0 |      1 |
| Singh C 2:017     |      0 |      0 |      0 |      1 |      0 |      1 |
| Brennan R 2:014   |      0 |      0 |      0 |      1 |      1 |      0 |
| Crane M 2:014     |      0 |      0 |      0 |      1 |      1 |      0 |
<BLANKLINE>
<BLANKLINE>



"""
from ... import vantagepoint
from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from ..documents_per_criterion import documents_per_criterion


def authors_production_over_time(
    topics_length=50,
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
    """Authors production over time."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        criterion="authors",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        cumulative=cumulative,
        **filters,
    )

    chart = vantagepoint.report.gantt_chart(
        terms_by_year,
        title="Authors' production over time",
    )

    chart.documents_per_author_ = documents_per_criterion(
        criterion="authors",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.production_per_year_ = indicators_by_topic_per_year(
        criterion="authors",
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart
