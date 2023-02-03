"""
Organizations' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__organizations_production_over_time.html"

>>> from techminer2 import bibliometrix
>>> pot = bibliometrix.organizations.organizations_production_over_time(
...    topics_length=10, 
...    directory=directory,
... )

>>> pot.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__organizations_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> pot.documents_per_organization_.head()
                                 organizations  ...                            doi
0               ---Teichmann International  AG  ...  10.1016/J.TECHSOC.2022.102150
1                           Harvard University  ...  10.1016/J.TECHSOC.2022.102150
2                        University of Messina  ...  10.1016/J.TECHSOC.2022.102150
3              Chinese University of Hong Kong  ...    10.1016/J.RIBAF.2022.101868
4  Nottingham University Business School China  ...    10.1016/J.RIBAF.2022.101868
<BLANKLINE>
[5 rows x 7 columns]

>>> pot.production_per_year_.head()
                                                         OCC  ...  local_citations_per_year
organizations                                      year       ...                          
---3PB                                             2022    1  ...                     0.500
---AML Forensic library KPMG Luxembourg Societe... 2020    1  ...                     0.750
---BITS Pilani                                     2020    1  ...                     0.750
---Centre for Law                                  2017    1  ...                     0.000
---Deloitte LLP                                    2018    1  ...                     0.833
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

    results = _Results()

    results.plot_ = _production_over_time(
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

    return results
