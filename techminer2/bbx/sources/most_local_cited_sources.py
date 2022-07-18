"""
Most Local Cited Sources (from reference lists)
===============================================================================

Plot the most local cited sources in the references.

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="source_abbr",
        directory=directory,
        database="references",
    )



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/most_local_cited_sources.html"

>>> from techminer2.bbx.sources import most_local_cited_sources
>>> most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/most_local_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...vp.report.chart import chart


def most_local_cited_sources(
    directory="./",
    top_n=20,
    plot="cleveland",
):
    """Most Local Cited Sources (from Reference Lists)."""

    return chart(
        column="source_abbr",
        directory=directory,
        top_n=top_n,
        min_occ=None,
        max_occ=None,
        title="Most Local Cited Sources (from Reference Lists)",
        plot=plot,
        database="references",
        metric="local_citations",
    )
