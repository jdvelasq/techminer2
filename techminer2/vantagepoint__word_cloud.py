"""
WordCloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/vantagepoint__word_cloud.png"


>>> from techminer2 import vantagepoint__word_cloud
>>> vantagepoint__word_cloud(
...     criterion='author_keywords',
...     title="Author Keywords",
...     topics_length=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../../images/vantagepoint__word_cloud.png
    :width: 900px
    :align: center

"""
from ._indicators.indicators_by_topic import indicators_by_topic
from ._plots.word_cloud_for_indicators import word_cloud_for_indicators


def vantagepoint__word_cloud(
    criterion,
    directory="./",
    database="documents",
    metric="OCC",
    start_year=None,
    end_year=None,
    topics_length=20,
    min_occ=None,
    max_occ=None,
    custom_topics=None,
    title=None,
    plot="bar",
    figsize=(12, 12),
    **filters,
):
    """Plots a word cloud from a dataframe."""

    indicators = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if custom_topics is None:
        custom_topics = indicators.copy()
        if min_occ is not None:
            custom_topics = custom_topics[custom_topics["OCC"] >= min_occ]
        if max_occ is not None:
            custom_topics = custom_topics[custom_topics["OCC"] <= max_occ]
        custom_topics = custom_topics.index.copy()
        custom_topics = custom_topics[:topics_length]
    else:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]

    indicators = indicators.loc[custom_topics, :]

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric=metric,
        title=title,
        figsize=figsize,
    )
