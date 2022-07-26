"""
Source Impact
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_impact.html"

>>> from techminer2 import bibliometrix__source_impact
>>> bibliometrix__source_impact(
...     impact_measure='h_index',
...     topics_length=20, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__impact import bibliometrix__impact


def bibliometrix__source_impact(
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=0,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by source."""

    return bibliometrix__impact(
        criterion="source_abbr",
        impact_measure=impact_measure,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Source Local Impact by " + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
