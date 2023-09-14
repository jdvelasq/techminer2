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

>>> from techminer2.performance.plots import terms_by_year
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> words.fig_.write_html("sphinx/_static/performance/words/descriptors/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/words/descriptors/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| descriptors                   |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 29:330                |      0 |      2 |      3 |      4 |      8 |      3 |      7 |      2 |
| REGULATORY_TECHNOLOGY 21:277  |      0 |      2 |      0 |      3 |      6 |      4 |      5 |      1 |
| FINANCIAL_INSTITUTIONS 16:198 |      0 |      0 |      2 |      2 |      5 |      3 |      4 |      0 |
| REGULATORY_COMPLIANCE 15:232  |      0 |      1 |      2 |      2 |      5 |      2 |      2 |      1 |
| FINANCIAL_REGULATION 12:395   |      1 |      2 |      1 |      1 |      1 |      2 |      4 |      0 |

>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
