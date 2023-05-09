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

>>> r.documents_per_organization_.head()
                                 organizations  ...                            doi
0               ---Teichmann International  AG  ...  10.1016/J.TECHSOC.2022.102150
1                           Harvard University  ...  10.1016/J.TECHSOC.2022.102150
2                        University of Messina  ...  10.1016/J.TECHSOC.2022.102150
3              Chinese University of Hong Kong  ...    10.1016/J.RIBAF.2022.101868
4  Nottingham University Business School China  ...    10.1016/J.RIBAF.2022.101868
<BLANKLINE>
[5 rows x 7 columns]

>>> r.production_per_year_.head()
                                                         OCC  ...  local_citations_per_year
organizations                                      year       ...                          
---3PB                                             2022    1  ...                     0.500
---AML Forensic library KPMG Luxembourg Societe... 2020    1  ...                     0.750
---BITS Pilani                                     2020    1  ...                     0.750
---Centre for Law                                  2017    1  ...                     0.000
---Deloitte LLP                                    2018    1  ...                     0.833
<BLANKLINE>
[5 rows x 7 columns]

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top 10
organizations with more documnets in a given bibliographic dataset. 
<BLANKLINE>
- Column 'OCC' is the number of documents published in a given year by the 
  current organization or institution. 
<BLANKLINE>
- Column 'Year' is the year of publication.
<BLANKLINE>
- Column 'Organization' is the organization or institution.
<BLANKLINE>
- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current organization during the 
  period of analysis.
<BLANKLINE>
| Organizations                          |   OCC |   Year |
|:---------------------------------------|------:|-------:|
| University of Hong Kong 3:185          |     2 |   2017 |
| University College Cork 3:041          |     1 |   2019 |
| University of Hong Kong 3:185          |     1 |   2020 |
| Ahlia University 3:019                 |     1 |   2020 |
| University College Cork 3:041          |     1 |   2018 |
| Ahlia University 3:019                 |     1 |   2021 |
| Ahlia University 3:019                 |     1 |   2022 |
| University College Cork 3:041          |     1 |   2022 |
| ---FinTech HK 2:161                    |     2 |   2017 |
| Coventry University 2:017              |     1 |   2020 |
| University of Westminster 2:017        |     1 |   2020 |
| Dublin City University 2:014           |     1 |   2020 |
| Coventry University 2:017              |     1 |   2022 |
| University of Westminster 2:017        |     1 |   2022 |
| Dublin City University 2:014           |     1 |   2021 |
| Politecnico di Milano 2:002            |     1 |   2020 |
| Politecnico di Milano 2:002            |     1 |   2022 |
| ---School of Electrical Engineering... |     2 |   2022 |
| ---3PB 1:003                           |     1 |   2022 |
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

    prompt_table = results.table_[
        ["organizations".replace("_", " ").title(), "OCC", "Year"]
    ]
    prompt_table = prompt_table.set_index("organizations".replace("_", " ").title())

    results.prompt_ = f"""
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top {topics_length}
organizations with more documnets in a given bibliographic dataset. 

- Column 'OCC' is the number of documents published in a given year by the 
  current organization or institution. 

- Column 'Year' is the year of publication.

- Column 'Organization' is the organization or institution.

- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current organization during the 
  period of analysis.

{prompt_table.to_markdown()}

Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 

Limit your description to a paragraph with no more than 250 words.    
"""

    return results
