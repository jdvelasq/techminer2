"""
Most Global Cited Countries
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_countries.html"


>>> from techminer2 import bibliometrix__most_global_cited_countries
>>> bibliometrix__most_global_cited_countries(
...     directory,
...     topics_length=20,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_global_cited_countries(
    directory="./",
    topics_length=20,
    plot="cleveland",
    database="documents",
    topic_min_occ=None,
    topic_min_citations=None,
    start_year=None,
    end_year=None,
    **filters,
):
    """Most global cited countries."""

    return vantagepoint__chart(
        criterion="countries",
        directory=directory,
        database=database,
        metric="global_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=None,
        topic_min_citations=None,
        custom_topics=None,
        title="Most Global Cited Countries",
        plot=plot,
        **filters,
    )
