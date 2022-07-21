"""
Institution Impact
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__institution_impact.html"

>>> from techminer2 import bibliometrix__institution_impact
>>> bibliometrix__institution_impact(
...     impact_measure='h_index', 
...     top_n=20, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__institution_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__impact import bibliometrix__impact


def bibliometrix__institution_impact(
    impact_measure="h_index",
    top_n=20,
    directory="./",
):
    """Plots the selected impact measure by institution."""

    return bibliometrix__impact(
        column="institutions",
        impact_measure=impact_measure,
        top_n=top_n,
        directory=directory,
        title="Institution Local Impact by " + impact_measure.replace("_", " ").title(),
    )
