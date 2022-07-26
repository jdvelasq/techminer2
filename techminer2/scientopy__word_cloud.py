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


**Trend Analysis.**

>>> from techminer2 import scientopy__word_cloud
>>> file_name = "sphinx/images/scientopy__word_cloud-6.png"
>>> scientopy__word_cloud(
...     criterion='author_keywords',
...     topics_length=20,
...     trend_analysis=True,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-6.png
    :width: 900px
    :align: center



>>> from techminer2._indicators.growth_indicators_by_topic import growth_indicators_by_topic
>>> growth_indicators_by_topic(
...     criterion="author_keywords", 
...     directory=directory,
... )[['OCC', 'average_growth_rate']].sort_values(['average_growth_rate', 'OCC'], ascending=False).head(20)
                                              OCC  average_growth_rate
author_keywords                                                       
semantic web                                    3                  0.5
smart contracts                                 3                  0.5
ethics                                          2                  0.5
china                                           2                  0.5
business models                                 2                  0.5
proptech (property + technology)                1                  0.5
register of processing activities               1                  0.5
regtech (regulation + technology)               1                  0.5
predictive analytics                            1                  0.5
regulatory enforcement                          1                  0.5
algorithmic transparency                        1                  0.5
technology trend analysis                       1                  0.5
terrorist financing                             1                  0.5
text mining                                     1                  0.5
unsupervised learning                           1                  0.5
ai-based systems                                1                  0.5
ai tools                                        1                  0.5
social network analysis                         1                  0.5
banking money laundering terrorist financing    1                  0.5
edutech (education + technology)                1                  0.5




"""
from ._indicators.growth_indicators_by_topic import growth_indicators_by_topic
from ._plots.word_cloud_for_indicators import word_cloud_for_indicators
from .scientopy__bar import _filter_indicators_by_custom_topics


def scientopy__word_cloud(
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

    indicators = growth_indicators_by_topic(
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
