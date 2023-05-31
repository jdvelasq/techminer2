"""
WordCloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/bibliometrix__word_cloud.png"


>>> from techminer2 import bibliometrix
>>> chart = bibliometrix.words.word_cloud(
...     criterion='author_keywords',
...     title="Author Keywords",
...     topics_length=50,
...     directory=directory,
... )
>>> chart.plot_.savefig(file_name)

.. image:: ../../../images/bibliometrix__word_cloud.png
    :width: 900px
    :align: center

"""
from ... import vantagepoint


def word_cloud(
    criterion,
    topics_length=250,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
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

    topics = vantagepoint.analyze.list_view(
        field=criterion,
        top_n=topics_length,
        occ_range=topic_min_occ,
        topic_occ_max=topic_max_occ,
        gc_range=topic_min_citations,
        topic_citations_max=topic_max_citations,
        items=custom_topics,
        root_dir=directory,
        metric=metric,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    return vantagepoint.report.word_cloud(
        topics,
        title=title,
        figsize=figsize,
    )
