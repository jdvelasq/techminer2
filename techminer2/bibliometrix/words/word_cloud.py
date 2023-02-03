"""
WordCloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/bibliometrix__word_cloud.png"


>>> from techminer2 import bibliometrix
>>> bibliometrix.words.word_cloud(
...     criterion='author_keywords',
...     title="Author Keywords",
...     topics_length=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../../../images/bibliometrix__word_cloud.png
    :width: 900px
    :align: center

"""
from ... import vantagepoint


def word_cloud(
    criterion,
    topics_length=250,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    metric="OCC",
    title=None,
    database="documents",
    #
    figsize=(12, 12),
    #
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots a word cloud from a dataframe."""

    return vantagepoint.report.word_cloud(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        metric=metric,
        title=title,
        database=database,
        #
        figsize=figsize,
        #
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
