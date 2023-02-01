"""
Word Cloud
===============================================================================


>>> directory = "data/regtech/"


**Basic Usage.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-1.png"
>>> scientopy.word_cloud(
...     criterion='author_keywords',
...     title="Author Keywords",
...     topics_length=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-1.png
    :width: 900px
    :align: center



**Time Filter.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-3.png"
>>> scientopy.word_cloud(
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

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-4.png"
>>> scientopy.word_cloud(
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

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-5.png"
>>> scientopy.word_cloud(
...     criterion='author_keywords',
...     custom_topics=[
...         "fintech",
...         "blockchain",
...         "financial regulation",
...         "innovation",
...     ],
...     directory=directory,
...     countries=["Australia", "United Kingdom", "United States"],
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-5.png
    :width: 900px
    :align: center


**Trend Analysis.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-6.png"
>>> scientopy.word_cloud(
...     criterion='author_keywords',
...     topics_length=20,
...     trend_analysis=True,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-6.png
    :width: 900px
    :align: center



>>> from techminer2.tm2__growth_indicators_by_topic import tm2__growth_indicators_by_topic
>>> tm2__growth_indicators_by_topic(
...     criterion="author_keywords", 
...     directory=directory,
... )[['OCC', 'average_growth_rate']].sort_values(['average_growth_rate', 'OCC'], ascending=False).head(20)
                             OCC  average_growth_rate
author_keywords                                      
challenges                     1                  0.5
online shareholder voting      1                  0.5
mifid ii                       1                  0.5
shareholder monitoring         1                  0.5
annual general meetings        1                  0.5
costs of voting                1                  0.5
companies                      1                  0.5
benefit                        1                  0.5
compliance                     7                  0.0
regtech                       28                 -0.5
fintech                       12                 -0.5
regulation                     5                 -0.5
innovation                     3                 -0.5
blockchain                     3                 -0.5
sandbox                        2                 -0.5
gdpr                           2                 -0.5
data protection officer        2                 -0.5
accountability                 2                 -0.5
anti money laundering (aml)    2                 -0.5
otc reform                     1                 -0.5




"""
from .._plots.word_cloud_for_indicators import word_cloud_for_indicators
from ..techminer.indicators.tm2__growth_indicators_by_topic import (
    tm2__growth_indicators_by_topic,
)
from .bar import _filter_indicators_by_custom_topics


def word_cloud(
    criterion,
    time_window=2,
    topics_length=50,
    custom_topics=None,
    trend_analysis=False,
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

    indicators = tm2__growth_indicators_by_topic(
        criterion=criterion,
        time_window=time_window,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if trend_analysis is True:
        indicators = indicators.sort_values(
            by=["average_growth_rate", "OCC", "global_citations"],
            ascending=[False, False, False],
        )
    else:
        indicators = indicators.sort_values(
            by=["OCC", "global_citations", "average_growth_rate"],
            ascending=[False, False, False],
        )

    indicators = _filter_indicators_by_custom_topics(
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
