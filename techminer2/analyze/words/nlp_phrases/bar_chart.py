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
...     field='nlp_phrases',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent NLP Phrases",
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
>>> chart.fig_.write_html("sphinx/_static/performance/words/nlp_phrases/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/words/nlp_phrases/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                        rank_occ  OCC  ...  between_2022_2023  growth_percentage
nlp_phrases                            ...                                      
REGULATORY_TECHNOLOGY          1   20  ...                6.0              30.00
FINANCIAL_INSTITUTIONS         2   15  ...                4.0              26.67
FINANCIAL_SYSTEM               3    8  ...                3.0              37.50
FINANCIAL_REGULATION           4    7  ...                1.0              14.29
REGULATORY_COMPLIANCE          5    7  ...                1.0              14.29
<BLANKLINE>
[5 rows x 5 columns]



>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
