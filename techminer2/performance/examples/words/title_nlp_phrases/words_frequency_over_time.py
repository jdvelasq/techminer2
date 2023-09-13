# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Word Frequency over Time
===============================================================================

>>> from techminer2.performance.plots import terms_by_year
>>> words = terms_by_year(
...     #
...     # PARAMS:
...     field="title_nlp_phrases",
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
>>> words.fig_.write_html("sphinx/_static/performance/words/title_nlp_phrases/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../_static/performance/words/title_nlp_phrases/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| title_nlp_phrases                   |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_TECHNOLOGY 3:020         |      0 |      0 |      0 |      0 |      1 |      2 |      0 |      0 |
| ARTIFICIAL_INTELLIGENCE 3:017       |      0 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| FINANCIAL_REGULATION 2:180          |      1 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
| FINANCIAL_CRIME 2:012               |      0 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| DIGITAL_REGULATORY_COMPLIANCE 1:033 |      0 |      0 |      0 |      1 |      0 |      0 |      0 |      0 |


>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
