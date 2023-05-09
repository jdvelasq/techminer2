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

>>> r.documents_per_source_.head()
          source_abbr  ...                             doi
0         TECHNOL SOC  ...   10.1016/J.TECHSOC.2022.102150
1  RES INT BUS FINANC  ...     10.1016/J.RIBAF.2022.101868
2            COMPUTER  ...         10.1109/MC.2022.3176693
3     FINANCIAL INNOV  ...      10.1186/S40854-021-00313-6
4       J CORP FINANC  ...  10.1016/J.JCORPFIN.2022.102276
<BLANKLINE>
[5 rows x 7 columns]


>>> r.production_per_year_.head()
                            OCC  ...  local_citations_per_year
source_abbr           year       ...                          
ACM INT CONF PROC SER 2021    1  ...                     0.000
ADELAIDE LAW REV      2020    1  ...                     0.250
ADV INTELL SYS COMPUT 2021    1  ...                     0.333
CEUR WORKSHOP PROC    2020    1  ...                     0.750
COMPUTER              2022    1  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top 10
sources with more documnets in a given bibliographic dataset. 
<BLANKLINE>
- Column 'OCC' is the number of documents published in a given year by the 
  current source. 
<BLANKLINE>
- Column 'Year' is the year of publication.
<BLANKLINE>
- Column 'Source Abbr' is the source abbreviation.
<BLANKLINE>
- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current source during the 
  period of analysis.
<BLANKLINE>
| Source Abbr                              |   OCC |   Year |
|:-----------------------------------------|------:|-------:|
| J BANK REGUL 2:035                       |     1 |   2020 |
| J BANK REGUL 2:035                       |     1 |   2021 |
| J FINANC CRIME 2:013                     |     1 |   2020 |
| J FINANC CRIME 2:013                     |     1 |   2022 |
| FOSTER INNOV AND COMPET WITH FINTECH,... |     2 |   2020 |
| STUD COMPUT INTELL 2:001                 |     2 |   2021 |
| INT CONF INF TECHNOL SYST INNOV,...      |     2 |   2022 |
| ROUTLEDGE HANDB OF FINANCIAL...          |     2 |   2021 |
| J FINANCIAL DATA SCI 1:005               |     1 |   2019 |
| J IND BUS ECON 1:001                     |     1 |   2022 |
| PROC INT CONF ELECTRON BUS (ICEB) 1:001  |     1 |   2017 |
| RES INT BUS FINANC 1:000                 |     1 |   2023 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.    
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

    prompt_table = results.table_[
        ["source_abbr".replace("_", " ").title(), "OCC", "Year"]
    ]
    prompt_table = prompt_table.set_index("source_abbr".replace("_", " ").title())

    results.prompt_ = f"""
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top {topics_length}
sources with more documnets in a given bibliographic dataset. 

- Column 'OCC' is the number of documents published in a given year by the 
  current source. 

- Column 'Year' is the year of publication.

- Column 'Source Abbr' is the source abbreviation.

- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current source during the 
  period of analysis.

{prompt_table.to_markdown()}

Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 

Limit your description to a paragraph with no more than 250 words.    
"""

    return results
