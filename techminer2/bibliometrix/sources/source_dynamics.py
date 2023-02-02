"""
Source Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_dynamics.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.sources.source_dynamics(
...     topics_length=10, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .._dynamics import _dynamics


def source_dynamics(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title="Source Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top sources."""

    return _dynamics(
        criterion="source_abbr",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        plot=plot,
        title=title,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
