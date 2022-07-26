"""
Most Relevant Organizations
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_relevant_organizations.html"

>>> from techminer2 import bibliometrix__most_relevant_organizations
>>> bibliometrix__most_relevant_organizations(
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_relevant_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_relevant_organizations(
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the number of documents by organizations using the specified plot."""

    return vantagepoint__chart(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Frequent Organizations",
        plot=plot,
        **filters,
    )
