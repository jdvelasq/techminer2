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



>>> r.documents_per_author_.head()
       authors  ...                            doi
0  Teichmann F  ...  10.1016/J.TECHSOC.2022.102150
1   Boticiu SR  ...  10.1016/J.TECHSOC.2022.102150
2     Sergi BS  ...  10.1016/J.TECHSOC.2022.102150
3        Lan G  ...    10.1016/J.RIBAF.2022.101868
4       Li D/1  ...    10.1016/J.RIBAF.2022.101868
<BLANKLINE>
[5 rows x 7 columns]

>>> r.production_per_year_.head()
                        OCC  ...  local_citations_per_year
authors           year       ...                          
Abdullah Y        2022    1  ...                     0.000
Ajmi JA           2021    1  ...                     0.333
Anagnostopoulos I 2018    1  ...                     2.833
Anasweh M         2020    1  ...                     1.000
Arman AA          2022    2  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]


>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top 10
authors with more documnets in a given bibliographic dataset. 
<BLANKLINE>
- Column 'OCC' is the number of documents published in a given year by the 
  current author. 
<BLANKLINE>
- Column 'Year' is the year of publication.
<BLANKLINE>
- Column 'Authors' is the current author's name.
<BLANKLINE>
- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current author during the 
  period of analysis.
<BLANKLINE>
| Authors          |   OCC |   Year |
|:-----------------|------:|-------:|
| Arner DW 3:185   |     2 |   2017 |
| Buckley RP 3:185 |     2 |   2017 |
| Arner DW 3:185   |     1 |   2020 |
| Buckley RP 3:185 |     1 |   2020 |
| Butler T/1 2:041 |     1 |   2019 |
| Lin W 2:017      |     1 |   2020 |
| Singh C 2:017    |     1 |   2020 |
| Brennan R 2:014  |     1 |   2020 |
| Crane M 2:014    |     1 |   2020 |
| Hamdan A 2:018   |     1 |   2020 |
| Sarea A 2:012    |     1 |   2020 |
| Butler T/1 2:041 |     1 |   2018 |
| Hamdan A 2:018   |     1 |   2021 |
| Lin W 2:017      |     1 |   2022 |
| Singh C 2:017    |     1 |   2022 |
| Brennan R 2:014  |     1 |   2021 |
| Crane M 2:014    |     1 |   2021 |
| Grassi L 2:002   |     1 |   2020 |
| Grassi L 2:002   |     1 |   2022 |
| Sarea A 2:012    |     1 |   2022 |
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
    documents_per_author_ = None


def authors_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Authors production over time."""

    results = _Results()

    results = _production_over_time(
        criterion="authors",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Authors' production over time",
        metric="OCC",
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.documents_per_author_ = _documents_per(
        criterion="authors",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = indicators_by_topic_per_year(
        criterion="authors",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    prompt_table = results.table_[["authors".replace("_", " ").title(), "OCC", "Year"]]
    prompt_table = prompt_table.set_index("authors".replace("_", " ").title())

    results.prompt_ = f"""
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top {topics_length}
authors with more documnets in a given bibliographic dataset. 

- Column 'OCC' is the number of documents published in a given year by the 
  current author. 

- Column 'Year' is the year of publication.

- Column 'Authors' is the current author's name.

- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current author during the 
  period of analysis.

{prompt_table.to_markdown()}

Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 

Limit your description to a paragraph with no more than 250 words.    
"""

    return results
