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
...     field="descriptors",
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
>>> words.fig_.write_html("sphinx/_static/analyze/words/descriptors/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/descriptors/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| descriptors                  |   2015 |   2016 |   2017 |   2018 |   2019 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|
| FINTECH 45:7063              |      0 |      7 |      9 |     15 |     14 |
| TECHNOLOGIES 26:4203         |      1 |      5 |      5 |      7 |      8 |
| FINANCE 22:3678              |      1 |      4 |      5 |      8 |      4 |
| INNOVATION 20:3223           |      1 |      4 |      5 |      6 |      4 |
| FINANCIAL_TECHNOLOGY 19:2615 |      0 |      2 |      2 |      6 |      9 |



>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
