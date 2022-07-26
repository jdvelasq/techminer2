"""
Organization Impact
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__organization_impact.html"

>>> from techminer2 import bibliometrix__organization_impact
>>> bibliometrix__organization_impact(
...     impact_measure='h_index', 
...     topics_length=20, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__organization_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__impact import bibliometrix__impact


def bibliometrix__organization_impact(
    impact_measure="h_index",
    topics_length=20,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by organizations."""

    return bibliometrix__impact(
        criterion="organizations",
        impact_measure=impact_measure,
        topics_length=topics_length,
        directory=directory,
        title="Organization Local Impact by "
        + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
