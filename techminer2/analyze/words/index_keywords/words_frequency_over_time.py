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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> words.fig_.write_html("sphinx/_static/analyze/words/index_keywords/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/index_keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| index_keywords              |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_COMPLIANCE 9:34  |      0 |      1 |      0 |      1 |      3 |      1 |      2 |      1 |
| FINANCIAL_INSTITUTIONS 6:09 |      0 |      0 |      0 |      0 |      3 |      1 |      2 |      0 |
| FINANCE 5:16                |      0 |      1 |      0 |      1 |      0 |      1 |      2 |      0 |
| REGTECH 5:15                |      0 |      2 |      0 |      1 |      0 |      0 |      2 |      0 |
| ANTI_MONEY_LAUNDERING 3:10  |      0 |      0 |      0 |      0 |      1 |      2 |      0 |      0 |

>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""