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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/word_trends.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
                        rank_occ  OCC  ...  between_2022_2023  growth_percentage
abstract_nlp_phrases                   ...                                      
REGULATORY_TECHNOLOGY          1   19  ...                6.0              31.58
FINANCIAL_INSTITUTIONS         2   15  ...                4.0              26.67
FINANCIAL_SYSTEM               3    8  ...                3.0              37.50
REGULATORY_COMPLIANCE          4    7  ...                1.0              14.29
FINANCIAL_SECTOR               5    7  ...                2.0              28.57
<BLANKLINE>
[5 rows x 5 columns]



>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
