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
...     field="abstract_nlp_phrases",
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
>>> words.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| abstract_nlp_phrases          |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_TECHNOLOGY 19:269  |      0 |      2 |      0 |      3 |      6 |      2 |      5 |      1 |
| FINANCIAL_INSTITUTIONS 16:224 |      1 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| FINANCIAL_CRISIS 12:235       |      1 |      1 |      1 |      1 |      3 |      2 |      2 |      1 |
| REGULATORY_COMPLIANCE 10:360  |      0 |      2 |      2 |      1 |      2 |      1 |      2 |      0 |
| FINANCIAL_SECTOR 09:196       |      0 |      1 |      0 |      0 |      2 |      4 |      2 |      0 |


>>> print(words.prompt_)  # doctest: +ELLIPSIS
Your task is ...






"""
