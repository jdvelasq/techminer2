"""
Most Frequent Words
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_words.html"

>>> from techminer2 import bibliometrix__most_frequent_words
>>> bibliometrix__most_frequent_words(
...     criterion="author_keywords",
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
...     database="documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>




"""
from .vantagepoint__chart import vantagepoint__chart


def bibliometrix__most_frequent_words(
    criterion="author_keywords",
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
    """Plots the number of documents by country using the specified plot."""

    return vantagepoint__chart(
        criterion=criterion,
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        min_occ_per_topic=min_occ_per_topic,
        min_citations_per_topic=min_citations_per_topic,
        custom_topics=None,
        title="Most Frequent Keywords",
        plot=plot,
        **filters,
    )
