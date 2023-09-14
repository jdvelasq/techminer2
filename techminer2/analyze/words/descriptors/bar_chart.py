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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/performance/words/descriptors/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/words/descriptors/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                        rank_occ  OCC  ...  between_2022_2023  growth_percentage
descriptors                            ...                                      
REGTECH                        1   29  ...                9.0              31.03
REGULATORY_TECHNOLOGY          2   21  ...                6.0              28.57
FINANCIAL_INSTITUTIONS         3   16  ...                4.0              25.00
REGULATORY_COMPLIANCE          4   15  ...                3.0              20.00
FINANCIAL_REGULATION           5   12  ...                4.0              33.33
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
