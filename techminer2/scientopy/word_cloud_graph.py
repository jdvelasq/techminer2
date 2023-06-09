# flake8: noqa
"""
Word Cloud Graph
===============================================================================


>>> root_dir = "data/regtech/"


**Basic Usage.**

>>> from techminer2 import scientopy
>>> file_name = "sphinx/images/scientopy__word_cloud-1.png"
>>> scientopy.word_cloud_graph(
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
>>> scientopy.word_cloud_graph(
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
>>> scientopy.word_cloud_graph(
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
>>> scientopy.word_cloud_graph(
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
>>> scientopy.word_cloud_graph(
...     field='author_keywords',
...     top_n=20,
...     is_trend_analysis=True,
...     root_dir=root_dir,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud-6.png
    :width: 900px
    :align: center



>>> from techminer2 import techminer
>>> techminer.indicators.growth_indicators_by_field(
...     field="author_keywords", 
...     root_dir=root_dir,
... )[['OCC', 'average_growth_rate']].sort_values(['average_growth_rate', 'OCC'], ascending=False).head(20)
                           OCC  average_growth_rate
author_keywords                                    
ANNUAL_GENERAL_MEETINGS      1                  0.5
BENEFIT                      1                  0.5
CHALLENGES                   1                  0.5
COMPANIES                    1                  0.5
COSTS_OF_VOTING              1                  0.5
MIFID_II                     1                  0.5
ONLINE_SHAREHOLDER_VOTING    1                  0.5
SHAREHOLDER_MONITORING       1                  0.5
COMPLIANCE                   7                  0.0
ARTIFICIAL_INTELLIGENCE      4                  0.0
FINANCIAL_REGULATION         4                  0.0
FINANCIAL_SERVICES           4                  0.0
RISK_MANAGEMENT              3                  0.0
SUPTECH                      3                  0.0
CHARITYTECH                  2                  0.0
DATA_PROTECTION              2                  0.0
ENGLISH_LAW                  2                  0.0
FINANCE                      2                  0.0
REPORTING                    2                  0.0
SMART_CONTRACT               2                  0.0


# pylint: disable=line-too-long
"""
from .._plots.word_cloud_for_indicators import word_cloud_for_indicators
from ..item_utils import generate_custom_items
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators.growth_indicators_by_field import (
    growth_indicators_by_field,
)
from .common import PROMPT, get_default_indicators, get_trend_indicators


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def word_cloud_graph(
    field,
    # Specific params:
    time_window=2,
    is_trend_analysis=False,
    title=None,
    figsize=(12, 12),
    n_words=50,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    if is_trend_analysis:
        return trend_analysis_word_cloud_graph(
            field=field,
            # Specific params:
            time_window=time_window,
            title=title,
            figsize=figsize,
            n_words=n_words,
            # Item filters:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return default_word_cloud_graph(
        field=field,
        # Specific params:
        time_window=time_window,
        title=title,
        figsize=figsize,
        n_words=n_words,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )


def default_word_cloud_graph(
    field,
    # Specific params:
    time_window,
    title,
    figsize,
    n_words,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    #
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    indicators = get_default_indicators(
        field=field,
        # Specific params:
        time_window=time_window,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric="OCC",
        title=title,
        figsize=figsize,
    )


def trend_analysis_word_cloud_graph(
    field,
    # Specific params:
    time_window,
    title,
    figsize,
    n_words,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    #
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    indicators = get_trend_indicators(
        field=field,
        # Specific params:
        time_window=time_window,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return word_cloud_for_indicators(
        dataframe=indicators,
        metric="OCC",
        title=title,
        figsize=figsize,
    )
