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
            rank_occ  OCC  before_2018  between_2018_2019  growth_percentage
words                                                                       
fintech            1   50           18                 32              64.00
financial          2   44           15                 29              65.91
©                  3   42           14                 28              66.67
technology         4   39           13                 26              66.67
new                5   26            9                 17              65.38


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
