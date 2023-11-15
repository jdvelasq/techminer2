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
...     field='descriptors',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Descriptors",
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
>>> chart.fig_.write_html("sphinx/_static/analyze/words/descriptors/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/descriptors/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                      rank_occ  OCC  ...  between_2018_2019  growth_percentage
descriptors                          ...                                      
FINTECH                      1   45  ...               29.0              64.44
TECHNOLOGIES                 2   26  ...               15.0              57.69
FINANCE                      3   22  ...               12.0              54.55
INNOVATION                   4   20  ...               10.0              50.00
FINANCIAL_TECHNOLOGY         5   19  ...               15.0              78.95
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
