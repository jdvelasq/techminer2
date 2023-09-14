# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bar Chart
===============================================================================


>>> from techminer2.performance.plots import bar_chart
>>> chart = bar_chart(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Author Keywords",
...     metric_label=None,
...     field_label=None,
...     #
...     # ITEM FILTERS:
...     top_n=20,
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/author_keywords/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/words/author_keywords/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                       rank_occ  OCC  ...  between_2022_2023  growth_percentage
author_keywords                       ...                                      
REGTECH                       1   28  ...                8.0              28.57
FINTECH                       2   12  ...                2.0              16.67
REGULATORY_TECHNOLOGY         3    7  ...                2.0              28.57
COMPLIANCE                    4    7  ...                2.0              28.57
REGULATION                    5    5  ...                1.0              20.00
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)  # doctest: +ELLIPSIS
Your task is ...



"""
