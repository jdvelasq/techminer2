"""
Source Dynamics
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_dynamics.html"

>>> from techminer2 import bibliometrix__source_dynamics
>>> bibliometrix__source_dynamics(
...     topics_length=10, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .bibliometrix__dynamics import bibliometrix__dynamics


def bibliometrix__source_dynamics(
    topics_length=10,
    min_occ_per_topic=None,
    min_citations_per_topic=0,
    directory="./",
    title="Source Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top sources."""

    return bibliometrix__dynamics(
        criterion="source_abbr",
        topics_length=topics_length,
        min_occ_per_topic=min_occ_per_topic,
        min_citations_per_topic=min_citations_per_topic,
        directory=directory,
        plot=plot,
        title=title,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
