# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Words Frequency over Time
===============================================================================

>>> from techminer2.analyze import terms_by_year
>>> words = terms_by_year(
...     #
...     # PARAMS:
...     field="keywords",
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
>>> words.fig_.write_html("sphinx/_static/analyze/words/keywords/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| keywords                   |   2015 |   2016 |   2017 |   2018 |   2019 |
|:---------------------------|-------:|-------:|-------:|-------:|-------:|
| FINTECH 32:5393            |      0 |      5 |      8 |     12 |      7 |
| FINANCE 11:1950            |      0 |      1 |      3 |      5 |      2 |
| FINANCIAL_SERVICES 08:1680 |      0 |      1 |      0 |      6 |      1 |
| INNOVATION 08:0990         |      0 |      3 |      3 |      1 |      1 |
| FINANCIAL_INDUSTRY 05:1272 |      0 |      0 |      2 |      3 |      0 |


>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
