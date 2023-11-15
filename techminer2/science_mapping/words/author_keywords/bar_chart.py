# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bar Chart
===============================================================================


>>> from techminer2.report import bar_chart
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/analyze/words/author_keywords/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/author_keywords/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                      rank_occ  OCC  ...  between_2018_2019  growth_percentage
author_keywords                      ...                                      
FINTECH                      1   31  ...                 18              58.06
INNOVATION                   2    7  ...                  1              14.29
FINANCIAL_SERVICES           3    4  ...                  3              75.00
FINANCIAL_TECHNOLOGY         4    4  ...                  3              75.00
BUSINESS                     5    3  ...                  3             100.00
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_)  # doctest: +ELLIPSIS
Your task is ...



"""
