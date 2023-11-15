# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Word Trends
===============================================================================


>>> from techminer2.analyze.words import word_trends
>>> chart = word_trends(
...     #
...     # ITEMS PARAMS:
...     field='abstract_nlp_phrases',
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     #
...     # CHART PARAMS:
...     title="Total Number of Documents, with Percentage of Documents Published in the Last Years",
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
>>> chart.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/word_trends.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head() 
                      rank_occ  OCC  ...  between_2018_2019  growth_percentage
abstract_nlp_phrases                 ...                                      
FINTECH                      1   32  ...               21.0              65.62
TECHNOLOGIES                 2   23  ...               14.0              60.87
AUTHOR                       3   18  ...               13.0              72.22
FINANCIAL_TECHNOLOGY         4   17  ...               14.0              82.35
FINANCIAL_INDUSTRY           5   16  ...                7.0              43.75
<BLANKLINE>
[5 rows x 5 columns]


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
