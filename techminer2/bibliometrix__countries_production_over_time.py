"""
Countries' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__countries_production_over_time.html"


>>> from techminer2 import bibliometrix__countries_production_over_time
>>> bibliometrix__countries_production_over_time(
...    topics_length=10,
...    directory=directory,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from dataclasses import dataclass

from .bibliometrix__documents_per import bibliometrix__documents_per
from .bibliometrix__production_over_time import bibliometrix__production_over_time
from .core.indicators.tm2__indicators_by_topic_per_year import (
    tm2__indicators_by_topic_per_year,
)


@dataclass(init=False)
class _Results:
    plot_ = None
    production_per_year_ = None
    documents_per_country_ = None


def bibliometrix__countries_production_over_time(
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

    results = _Results()

    results.plot_ = bibliometrix__production_over_time(
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

    results.documents_per_country_ = bibliometrix__documents_per(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = tm2__indicators_by_topic_per_year(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    return results
