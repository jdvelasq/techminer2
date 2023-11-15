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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/analyze/words/nlp_phrases/bar_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/nlp_phrases/bar_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.df_.head()
                      rank_occ  OCC  ...  between_2018_2019  growth_percentage
nlp_phrases                          ...                                      
FINTECH                      1   40  ...               25.0              62.50
TECHNOLOGIES                 2   23  ...               14.0              60.87
AUTHOR                       3   18  ...               13.0              72.22
FINANCIAL_INDUSTRY           4   17  ...                8.0              47.06
FINANCIAL_TECHNOLOGY         5   17  ...               14.0              82.35
<BLANKLINE>
[5 rows x 5 columns]



>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
