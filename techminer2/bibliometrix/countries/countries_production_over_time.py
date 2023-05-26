"""
Countries' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__countries_production_over_time.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.countries_production_over_time(
...    topics_length=10,
...    directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(r.documents_per_country_.head().to_markdown())
|    | countries     | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:--------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Italy         | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Switzerland   | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | United States | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | China         | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | United States | RegTech's Rise                                                                               |   2022 | Computer                                       |                  0 |                 0 | 10.1109/MC.2022.3176693       |


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
Analyze the table below which contains the  occurrences by year for the countries. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
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



"""
from ... import vantagepoint
from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from ..documents_per_criterion import documents_per_criterion


def countries_production_over_time(
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
    """Country production over time."""

    terms_by_year = vantagepoint.analyze.terms_by_year(
        criterion="countries",
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
        cummulative=cumulative,
        **filters,
    )

    chart = vantagepoint.report.gantt_chart(
        terms_by_year,
        title="Contry' production over time",
    )

    chart.documents_per_country_ = documents_per_criterion(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.production_per_year_ = indicators_by_topic_per_year(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    chart.table_ = terms_by_year.table_.copy()

    return chart
