"""
Country Impact
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_impact.html"


>>> from techminer2 import bibliometrix__country_impact
>>> bibliometrix__country_impact(
...     impact_measure='h_index', 
...     top_n=20, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__impact import bibliometrix__impact


def bibliometrix__country_impact(
    impact_measure="h_index",
    top_n=20,
    directory="./",
):
    """Plots the selected impact measure by country."""

    return bibliometrix__impact(
        column="countries",
        impact_measure=impact_measure,
        top_n=top_n,
        directory=directory,
        title="Country Local Impact by " + impact_measure.replace("_", " ").title(),
    )
