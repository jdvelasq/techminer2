"""
Author Impact
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__author_impact.html"

>>> from techminer2 import bibliometrix__author_impact
>>> bibliometrix__author_impact(
...     impact_measure='h_index',
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__author_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__impact import bibliometrix__impact


def bibliometrix__author_impact(
    impact_measure="h_index",
    top_n=20,
    directory="./",
):
    """Plots the selected impact measure by author."""

    return bibliometrix__impact(
        column="authors",
        impact_measure=impact_measure,
        top_n=top_n,
        directory=directory,
        title="Author Local Impact by " + impact_measure.replace("_", " ").title(),
    )
