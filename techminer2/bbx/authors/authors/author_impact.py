"""
Author Impact
===============================================================================

See :doc:`impact indicators <impact_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/author_impact.html"

>>> from techminer2.bbx.authors.authors import author_impact
>>> author_impact(
...     impact_measure='h_index',
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/author_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from ....impact import impact


def author_impact(
    impact_measure="h_index",
    top_n=20,
    directory="./",
):
    """Plots the selected impact measure by author."""
    return impact(
        column="authors",
        impact_measure=impact_measure,
        top_n=top_n,
        directory=directory,
        title="Author Local Impact by " + impact_measure.replace("_", " ").title(),
    )
