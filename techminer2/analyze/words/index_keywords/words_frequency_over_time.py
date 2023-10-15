# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Word Frequency over Time
===============================================================================

>>> from techminer2.analyze import terms_by_year
>>> words = terms_by_year(
...     #
...     # PARAMS:
...     field="index_keywords",
...     cumulative=False,
...     #
...     # CHART PARAMS:
...     title=None,
...     #
...     # ITEM FILTERS:
...     top_n=5,
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
>>> words.fig_.write_html("sphinx/_static/analyze/words/index_keywords/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/index_keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| index_keywords             |   2015 |   2016 |   2017 |   2018 |   2019 |
|:---------------------------|-------:|-------:|-------:|-------:|-------:|
| FINANCE 10:1866            |      0 |      1 |      2 |      5 |      2 |
| FINTECH 10:1412            |      0 |      1 |      2 |      5 |      2 |
| FINANCIAL_SERVICES 05:1115 |      0 |      0 |      0 |      4 |      1 |
| FINANCIAL_INDUSTRY 04:1019 |      0 |      0 |      1 |      3 |      0 |
| COMMERCE 03:0846           |      0 |      0 |      1 |      1 |      1 |


>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
