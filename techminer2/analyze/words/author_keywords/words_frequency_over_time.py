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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> words.fig_.write_html("sphinx/_static/analyze/words/author_keywords/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/author_keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| author_keywords              |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      0 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037 |      0 |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030            |      0 |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164            |      0 |      0 |      2 |      0 |      1 |      1 |      1 |      0 |

>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
