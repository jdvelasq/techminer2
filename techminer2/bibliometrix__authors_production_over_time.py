"""
Authors' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__authors_production_over_time.html"


>>> from techminer2 import bibliometrix__authors_production_over_time
>>> pot = bibliometrix__authors_production_over_time(
...    topics_length=10,
...    directory=directory,
... )

>>> pot.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> pot.documents_per_author_.head()
        authors  ...                           doi
0   von Solms J  ...    10.1057/S41261-020-00134-0
1   Dashottar S  ...    10.1057/S41261-020-00127-Z
2  Srivastava V  ...    10.1057/S41261-020-00127-Z
3       Turki M  ...  10.1007/978-981-15-3383-9_32
4      Hamdan A  ...  10.1007/978-981-15-3383-9_32
<BLANKLINE>
[5 rows x 7 columns]


>>> pot.production_per_year_.head()
                   OCC  ...  local_citations_per_year
authors      year       ...                          
Abdullah Y   2022    1  ...                     0.000
Abi-Lahoud E 2018    1  ...                     0.000
Ajmi JA      2021    1  ...                     0.500
Al Haider N  2020    1  ...                     0.333
Alam TM      2021    1  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]



"""
from dataclasses import dataclass

from ._indicators.indicators_by_topic_per_year import indicators_by_topic_per_year
from .bibliometrix__documents_per import bibliometrix__documents_per
from .bibliometrix__production_over_time import bibliometrix__production_over_time


@dataclass(init=False)
class _Results:
    plot_ = None
    production_per_year_ = None
    documents_per_author_ = None


def bibliometrix__authors_production_over_time(
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

    results.plot_ = bibliometrix__production_over_time(
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

    results.documents_per_author_ = bibliometrix__documents_per(
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
