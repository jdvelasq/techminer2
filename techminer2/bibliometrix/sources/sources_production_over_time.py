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
|  3 | FINANCIAL INNOV    | Fintech, regtech, and financial development: evidence from China                                    |   2022 | Financial Innovation                           |                 13 |                 1 | 10.1186/S40854-021-00313-6     |
|  4 | J CORP FINANC      | Too much to learn? The (un)intended consequences of RegTech development on mergers and acquisitions |   2022 | Journal of Corporate Finance                   |                  0 |                 0 | 10.1016/J.JCORPFIN.2022.102276 |

>>> print(r.production_per_year_.head().to_markdown())
|                                 |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:--------------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('ACM INT CONF PROC SER', 2021) |     1 |         1 |                  2 |                 0 |     3 |                       0.667 |                      0     |
| ('ADELAIDE LAW REV', 2020)      |     1 |         1 |                  5 |                 1 |     4 |                       1.25  |                      0.25  |
| ('ADV INTELL SYS COMPUT', 2021) |     1 |         1 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('CEUR WORKSHOP PROC', 2020)    |     1 |         1 |                  2 |                 3 |     4 |                       0.5   |                      0.75  |
| ('COMPUTER', 2022)              |     1 |         1 |                  0 |                 0 |     2 |                       0     |                      0     |


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on document production by year per document source for the top 10 most productive sources in the dataset. Use the information in the table to draw conclusions about the productivity per year of the sources. The final part of the source name contains two numbers separated by a colon. The first is the total number of documents of the source, and the second is the total number of citations of the source. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| Source Abbr                              |   2017 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|
| FOSTER INNOV AND COMPET WITH FINTECH,... |      0 |      0 |      2 |      0 |      0 |      0 |
| INT CONF INF TECHNOL SYST INNOV,...      |      0 |      0 |      0 |      0 |      2 |      0 |
| J BANK REGUL 2:035                       |      0 |      0 |      1 |      1 |      0 |      0 |
| J FINANC CRIME 2:013                     |      0 |      0 |      1 |      0 |      1 |      0 |
| J FINANCIAL DATA SCI 1:005               |      0 |      1 |      0 |      0 |      0 |      0 |
| J IND BUS ECON 1:001                     |      0 |      0 |      0 |      0 |      1 |      0 |
| PROC INT CONF ELECTRON BUS (ICEB) 1:001  |      1 |      0 |      0 |      0 |      0 |      0 |
| RES INT BUS FINANC 1:000                 |      0 |      0 |      0 |      0 |      0 |      1 |
| ROUTLEDGE HANDB OF FINANCIAL...          |      0 |      0 |      0 |      2 |      0 |      0 |
| STUD COMPUT INTELL 2:001                 |      0 |      0 |      0 |      2 |      0 |      0 |
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
    documents_per_source_ = None


def sources_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Sources production over time."""

    results = _production_over_time(
        criterion="source_abbr",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Sources' production over time",
        metric="OCC",
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.documents_per_source_ = _documents_per(
        criterion="source_abbr",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = indicators_by_topic_per_year(
        criterion="source_abbr",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    table = results.table_.copy()
    table = table[["Source Abbr", "Year", "OCC"]]
    table = table.pivot(index="Source Abbr", columns="Year", values="OCC")
    table = table.fillna(0)
    results.prompt_ = _create_prompt(table)

    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on document production by year per document source for the top {table.shape[0]} \
most productive sources in the dataset. Use the information in the table to \
draw conclusions about the productivity per year of the sources. The final \
part of the source name contains two numbers separated by a colon. The first \
is the total number of documents of the source, and the second is the total \
number of citations of the source. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
