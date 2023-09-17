# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Frequent Words
===============================================================================


>>> from techminer2.analyze import performance_metrics
>>> metrics = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='title_noun_phrases',
...     metric="OCC",
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=10,
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
>>> print(metrics.df_.to_markdown())
| title_noun_phrases            |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGULATORY_TECHNOLOGY         |          1 |     3 |             3 |                   0 |                0    |
| ARTIFICIAL_INTELLIGENCE       |          2 |     3 |             2 |                   1 |               33.33 |
| FINANCIAL_REGULATION          |          3 |     2 |             2 |                   0 |                0    |
| FINANCIAL_CRIME               |          4 |     2 |             2 |                   0 |                0    |
| DIGITAL_REGULATORY_COMPLIANCE |          5 |     1 |             1 |                   0 |                0    |
| UNDERSTANDING_REGTECH         |          6 |     1 |             1 |                   0 |                0    |
| BANK_FAILURES                 |          7 |     1 |             1 |                   0 |                0    |
| CONCEPT_ARTICLE               |          8 |     1 |             1 |                   0 |                0    |
| REALISTIC_PROTECTION          |          9 |     1 |             1 |                   0 |                0    |
| EUROPEAN_UNION                |         10 |     1 |             1 |                   0 |                0    |




>>> metrics.fig_.write_html("sphinx/_static/analyze/words/title_noun_phrases/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/title_noun_phrases/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
