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
...     field='words',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Words",
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
>>> chart.fig_.write_html("sphinx/_static/analyze/words/words/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/words/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                       rank_occ  OCC  ...  between_2022_2023  growth_percentage
words                                 ...                                      
REGTECH                       1   48  ...                 12              25.00
REGULATORS                    2   30  ...                  9              30.00
NEW_TECHNOLOGIES              3   22  ...                  7              31.82
REGULATORY_TECHNOLOGY         4   20  ...                  6              30.00
COMPLIANCE                    5   18  ...                  3              16.67
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
