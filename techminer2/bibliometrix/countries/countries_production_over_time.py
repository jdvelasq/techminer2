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


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on document production by year per country for the top 10 most productive countries in the dataset. Use the information in the table to draw conclusions about the productivity per year of the countries. The final part of the country name contains two numbers separated by a colon. The first \ 
is the total number of documents of the country, and the second is the total number of citations of the country. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| Countries            |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| Australia 7:199      |      0 |      2 |      0 |      0 |      3 |      2 |      0 |      0 |
| Bahrain 4:019        |      0 |      0 |      0 |      0 |      1 |      2 |      1 |      0 |
| China 5:027          |      0 |      1 |      0 |      0 |      0 |      0 |      3 |      1 |
| Germany 4:051        |      0 |      0 |      1 |      0 |      2 |      0 |      1 |      0 |
| Hong Kong 3:185      |      0 |      2 |      0 |      0 |      1 |      0 |      0 |      0 |
| Ireland 5:055        |      0 |      0 |      1 |      1 |      1 |      1 |      1 |      0 |
| Italy 5:005          |      0 |      0 |      0 |      1 |      1 |      1 |      1 |      1 |
| Switzerland 4:045    |      0 |      1 |      1 |      0 |      1 |      0 |      0 |      1 |
| United Kingdom 7:199 |      0 |      0 |      3 |      1 |      2 |      0 |      1 |      0 |
| United States 6:059  |      1 |      0 |      1 |      2 |      0 |      0 |      1 |      1 |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>



"""
from dataclasses import dataclass

from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from .._documents_per import _documents_per
from .._production_over_time import _production_over_time


@dataclass(init=False)
class _Results:
    plot_ = None
    prompt_ = None
    production_per_year_ = None
    documents_per_country_ = None


def countries_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Country production over time."""

    results = _production_over_time(
        criterion="countries",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Country' production over time",
        metric="OCC",
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.documents_per_country_ = _documents_per(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = indicators_by_topic_per_year(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    table = results.table_.copy()
    table = table[["Countries", "Year", "OCC"]]
    table = table.pivot(index="Countries", columns="Year", values="OCC")
    table = table.fillna(0)
    results.prompt_ = _create_prompt(table)

    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on document production by year per country for the top {table.shape[0]} \
most productive countries in the dataset. Use the information in the table to \
draw conclusions about the productivity per year of the countries. The final \
part of the country name contains two numbers separated by a colon. The first \ 
is the total number of documents of the country, and the second is the total \
number of citations of the country. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
