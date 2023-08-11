# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance_analysis.keywords.word_cloud:

Word Cloud
===============================================================================

>>> from techminer2.performance_analysis.keywords import word_cloud
>>> chart = word_cloud(
...     #
...     # PERFORMANCE PARAMS:
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Keywords",
...     width=400, 
...     height=400,
...     #
...     # ITEM FILTERS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.save("sphinx/_static/performance/keywords/word_cloud.png")

.. image:: ../../../../_static/performance/keywords/word_cloud.png
    :width: 900px
    :align: center


"""
from ...gp_word_cloud import gp_word_cloud

UNIT_OF_ANALISIS = "abstract_nlp_phrases"


def word_cloud(
    #
    # PERFORMANCE PARAMS:
    metric="OCC",
    #
    # CHART PARAMS:
    width=400,
    height=400,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    return gp_word_cloud(
        #
        # PERFORMANCE PARAMS:
        field=UNIT_OF_ANALISIS,
        metric=metric,
        #
        # CHART PARAMS:
        width=width,
        height=height,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
