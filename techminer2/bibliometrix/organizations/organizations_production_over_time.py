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


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on document production by year per organization for the top 10 most productive organizations in the dataset. Use the information in the table to draw conclusions about the productivity per year of the organizations. The final part of the organization name contains two numbers separated by a colon. The first \ 
is the total number of documents of the organization, and the second is the total number of citations of the organization. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| Organizations                          |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:---------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| ---3PB 1:003                           |      0 |      0 |      0 |      0 |      0 |      1 |
| ---FinTech HK 2:161                    |      2 |      0 |      0 |      0 |      0 |      0 |
| ---School of Electrical Engineering... |      0 |      0 |      0 |      0 |      0 |      2 |
| Ahlia University 3:019                 |      0 |      0 |      0 |      1 |      1 |      1 |
| Coventry University 2:017              |      0 |      0 |      0 |      1 |      0 |      1 |
| Dublin City University 2:014           |      0 |      0 |      0 |      1 |      1 |      0 |
| Politecnico di Milano 2:002            |      0 |      0 |      0 |      1 |      0 |      1 |
| University College Cork 3:041          |      0 |      1 |      1 |      0 |      0 |      1 |
| University of Hong Kong 3:185          |      2 |      0 |      0 |      1 |      0 |      0 |
| University of Westminster 2:017        |      0 |      0 |      0 |      1 |      0 |      1 |
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
    documents_per_organization_ = None


def organizations_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Institution production over time."""

    results = _production_over_time(
        criterion="organizations",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Organizations' production over time",
        metric="OCC",
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.documents_per_organization_ = _documents_per(
        criterion="organizations",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = indicators_by_topic_per_year(
        criterion="organizations",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    table = results.table_.copy()
    table = table[["Organizations", "Year", "OCC"]]
    table = table.pivot(index="Organizations", columns="Year", values="OCC")
    table = table.fillna(0)
    results.prompt_ = _create_prompt(table)

    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on document production by year per organization for the top {table.shape[0]} \
most productive organizations in the dataset. Use the information in the table to \
draw conclusions about the productivity per year of the organizations. The final \
part of the organization name contains two numbers separated by a colon. The first \ 
is the total number of documents of the organization, and the second is the total \
number of citations of the organization. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
