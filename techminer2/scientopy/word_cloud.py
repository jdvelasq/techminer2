# flake8: noqa
"""
Word Cloud
===============================================================================


>>> root_dir = "data/regtech/"


**Basic Usage.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-1.png"
>>> scientopy.word_cloud(
...     field='author_keywords',
...     title="Author Keywords",
...     top_n=50,
...     root_dir=root_dir,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-1.png
    :width: 900px
    :align: center



**Time Filter.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-3.png"
>>> scientopy.word_cloud(
...     field='author_keywords',
...     title="Author Keywords",
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-3.png
    :width: 900px
    :align: center


**Custom Topics Extraction.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-4.png"
>>> scientopy.word_cloud(
...     field='author_keywords',
...     custom_items=[
...         "FINTECH",
...         "BLOCKCHAIN",
...         "FINANCIAL_REGULATION",
...         "MACHINE_LEARNING",
...         "BIG_DATA",
...         "CRYPTOCURRENCY",
...     ],
...     root_dir=root_dir,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-4.png
    :width: 900px
    :align: center


**Filters (previous search results).**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-5.png"
>>> scientopy.word_cloud(
...     field='author_keywords',
...     custom_items=[
...         "FINTECH",
...         "BLOCKCHAIN",
...         "FINANCIAL_REGULATION",
...         "MACHINE_LEARNING",
...         "BIG_DATA",
...         "CRYPTOCURRENCY",
...     ],
...     root_dir=root_dir,
...     countries=["Australia", "United Kingdom", "United States"],
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-5.png
    :width: 900px
    :align: center


**Trend Analysis.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-6.png"
>>> scientopy.word_cloud(
...     field='author_keywords',
...     top_n=20,
...     trend_analysis=True,
...     root_dir=root_dir,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-6.png
    :width: 900px
    :align: center



>>> from techminer2 import techminer
>>> techminer.indicators.growth_indicators_by_topic(
...     field="author_keywords", 
...     root_dir=root_dir,
... )[['OCC', 'average_growth_rate']].sort_values(['average_growth_rate', 'OCC'], ascending=False).head(20)
                           OCC  average_growth_rate
author_keywords                                    
MIFID_II                     1                  0.5
SHAREHOLDER_MONITORING       1                  0.5
ONLINE_SHAREHOLDER_VOTING    1                  0.5
CHALLENGES                   1                  0.5
COMPANIES                    1                  0.5
BENEFIT                      1                  0.5
ANNUAL_GENERAL_MEETINGS      1                  0.5
COSTS_OF_VOTING              1                  0.5
COMPLIANCE                   7                  0.0
REGTECH                     28                 -0.5
FINTECH                     12                 -0.5
REGULATION                   5                 -0.5
REGULATORY_TECHNOLOGY        3                 -0.5
INNOVATION                   3                 -0.5
BLOCKCHAIN                   3                 -0.5
SANDBOXES                    2                 -0.5
DATA_PROTECTION_OFFICER      2                 -0.5
GDPR                         2                 -0.5
ACCOUNTABILITY               2                 -0.5
TRUST                        1                 -0.5


# pylint: disable=line-too-long
"""
from .._plots.word_cloud_for_indicators import word_cloud_for_indicators
from ..techminer.indicators.growth_indicators_by_topic import (
    growth_indicators_by_topic,
)
from .bar import _filter_indicators_by_custom_topics


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def word_cloud(
    field,
    # Specific params:
    time_window=2,
    trend_analysis=False,
    title=None,
    figsize=(12, 12),
    # Item filters:
    top_n=50,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots a word cloud from a dataframe."""

    indicators = growth_indicators_by_topic(
        field=field,
        time_window=time_window,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
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
        topics_length=top_n,
        custom_topics=custom_items,
    )

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric="OCC",
        title=title,
        figsize=figsize,
    )
