"""
Word Cloud (ok!)
===============================================================================


>>> directory = "data/regtech/"


**Basic Usage.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-1.png"
>>> scientopy__word_cloud(
...     criterion='author_keywords',
...     title="Author Keywords",
...     topics_length=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-1.png
    :width: 900px
    :align: center



**Time Filter.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-3.png"
>>> scientopy__word_cloud(
...     criterion='author_keywords',
...     title="Author Keywords",
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-3.png
    :width: 900px
    :align: center


**Custom Topics Extraction.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-4.png"
>>> scientopy__word_cloud(
...     criterion='author_keywords',
...     custom_topics=[
...         "fintech",
...         "blockchain",
...         "financial regulation",
...         "machine learning",
...         "big data",
...         "cryptocurrency",
...     ],
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-4.png
    :width: 900px
    :align: center


**Filters (previous search results).**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-5.png"
>>> scientopy__word_cloud(
...     criterion='author_keywords',
...     custom_topics=[
...         "fintech",
...         "blockchain",
...         "financial regulation",
...         "machine learning",
...         "big data",
...         "cryptocurrency",
...     ],
...     directory=directory,
...     countries=["United States"],
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-5.png
    :width: 900px
    :align: center




"""
from ._indicators.indicators_by_topic import indicators_by_topic
from ._plots.word_cloud_for_indicators import word_cloud_for_indicators
from .scientopy__bar import _filter_indicators


def scientopy__word_cloud(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    #
    title=None,
    figsize=(12, 12),
    #
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
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

    if topic_min_occ is not None:
        indicators = indicators[indicators.OCC >= topic_min_occ]
    if topic_min_citations is not None:
        indicators = indicators[indicators.global_citations >= topic_min_citations]

    indicators = _filter_indicators(
        indicators=indicators,
        topics_length=topics_length,
        custom_topics=custom_topics,
    )

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric="OCC",
        title=title,
        figsize=figsize,
    )
