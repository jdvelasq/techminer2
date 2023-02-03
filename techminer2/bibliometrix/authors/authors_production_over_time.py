"""
Authors' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__authors_production_over_time.html"


>>> from techminer2 import bibliometrix
>>> pot = bibliometrix.authors.authors_production_over_time(
...    topics_length=10,
...    directory=directory,
... )

>>> pot.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> pot.documents_per_author_.head()
       authors  ...                            doi
0  Teichmann F  ...  10.1016/J.TECHSOC.2022.102150
1   Boticiu SR  ...  10.1016/J.TECHSOC.2022.102150
2     Sergi BS  ...  10.1016/J.TECHSOC.2022.102150
3        Lan G  ...    10.1016/J.RIBAF.2022.101868
4       Li D/1  ...    10.1016/J.RIBAF.2022.101868
<BLANKLINE>
[5 rows x 7 columns]

>>> pot.production_per_year_.head()
                        OCC  ...  local_citations_per_year
authors           year       ...                          
Abdullah Y        2022    1  ...                     0.000
Ajmi JA           2021    1  ...                     0.333
Anagnostopoulos I 2018    1  ...                     2.833
Anasweh M         2020    1  ...                     1.000
Arman AA          2022    2  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]


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

    results.plot_ = _production_over_time(
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

    return results
