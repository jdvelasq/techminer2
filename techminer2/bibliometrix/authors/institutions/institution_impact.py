"""
Institution Impact
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/institution_impact.html"

>>> from techminer2 import institution_impact
>>> institution_impact(
...     impact_measure='h_index', 
...     top_n=20, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/institution_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...impact import impact


def institution_impact(
    impact_measure="h_index",
    top_n=20,
    directory="./",
):
    """Plots the selected impact measure by institution."""
    return impact(
        column="institutions",
        impact_measure=impact_measure,
        top_n=top_n,
        directory=directory,
        title="Institution Local Impact by " + impact_measure.replace("_", " ").title(),
    )
