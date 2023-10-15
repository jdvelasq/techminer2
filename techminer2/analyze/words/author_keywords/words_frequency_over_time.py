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
...     field="author_keywords",
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
>>> words.fig_.write_html("sphinx/_static/analyze/words/author_keywords/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/author_keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| author_keywords                         |   2015 |   2016 |   2017 |   2018 |   2019 |
|:----------------------------------------|-------:|-------:|-------:|-------:|-------:|
| FINTECH 31:5168                         |      0 |      5 |      8 |     12 |      6 |
| INNOVATION 07:0911                      |      0 |      3 |      3 |      1 |      0 |
| FINANCIAL_SERVICES 04:0667              |      0 |      1 |      0 |      3 |      0 |
| FINANCIAL_TECHNOLOGY 04:0551            |      0 |      0 |      1 |      1 |      2 |
| MOBILE_FINTECH_PAYMENT_SERVICES 04:0485 |      0 |      1 |      0 |      2 |      1 |



>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
