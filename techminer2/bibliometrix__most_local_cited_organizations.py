"""
Most Local Cited Institutions
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_organizations.html"

>>> from techminer2 import bibliometrix__most_local_cited_organizations
>>> bibliometrix__most_local_cited_organizations(
...     topics_length=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_local_cited_organizations(
    directory="./",
    topics_length=20,
    min_occ_per_topic=None,
    min_citations_per_topic=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most Local Cited Organizations (from Reference Lists)."""

    return vantagepoint__chart(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="local_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        min_occ_per_topic=min_occ_per_topic,
        min_citations_per_topic=min_citations_per_topic,
        custom_topics=None,
        title="Most Local Cited Organizations (from Reference Lists)",
        plot=plot,
        **filters,
    )
