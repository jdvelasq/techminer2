"""
Word Cloud
===============================================================================


>>> directory = "data/regtech/"


**Basic Usage.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-1.png"
>>> scientopy__word_cloud(
...     column='author_keywords',
...     title="Author Keywords",
...     topics_length=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-1.png
    :width: 900px
    :align: center

**'skip_first' argument.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-2.png"
>>> scientopy__word_cloud(
...     column='author_keywords',
...     title="Author Keywords",
...     skip_first=5,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-2.png
    :width: 900px
    :align: center


**Time Filter.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-3.png"
>>> scientopy__word_cloud(
...     column='author_keywords',
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
...     column='author_keywords',
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


"""
from ._plots.word_cloud_for_indicators import word_cloud_for_indicators

# from .scientopy__bar import _compute_indicators, _filter_indicators


def scientopy__word_cloud(
    column,
    start_year=None,
    end_year=None,
    topics_length=50,
    skip_first=0,
    custom_topics=None,
    title=None,
    directory="./",
    database="documents",
    #
    figsize=(12, 12),
):
    """Plots a word cloud from a dataframe."""

    indicators = _compute_indicators(
        directory=directory,
        column=column,
        database=database,
        start_year=start_year,
        end_year=end_year,
    )

    indicators = _filter_indicators(
        indicators=indicators,
        topics_length=topics_length,
        skip_first=skip_first,
        custom_topics=custom_topics,
    )

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric="OCC",
        title=title,
        figsize=figsize,
    )
