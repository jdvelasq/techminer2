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
...     field='title_nlp_phrases',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title="Most Frequent Title NLP Phrases",
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
>>> chart.fig_.write_html("sphinx/_static/analyze/words/title_nlp_phrases/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/title_nlp_phrases/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                   rank_occ  OCC  ...  between_2018_2019  growth_percentage
title_nlp_phrases                 ...                                      
FINTECH                   1   27  ...               17.0              62.96
BANKING                   2    7  ...                4.0              57.14
CHINA                     3    5  ...                2.0              40.00
IMPACT                    4    4  ...                3.0              75.00
CHALLENGES                5    3  ...                2.0              66.67
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...





"""
