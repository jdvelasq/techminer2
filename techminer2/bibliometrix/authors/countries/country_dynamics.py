"""
Country Dynamics
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_dynamics.html"


>>> from techminer2 import bibliometrix__country_dynamics
>>> bibliometrix__country_dynamics(
...     topics_length=5, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_dynamics.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...dynamics import bibliometrix__dynamics


def bibliometrix__country_dynamics(
    topics_length=5,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title="Country Dynamics",
    plot=True,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a dynamics chat for top sources."""

    return bibliometrix__dynamics(
        criterion="countries",
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
