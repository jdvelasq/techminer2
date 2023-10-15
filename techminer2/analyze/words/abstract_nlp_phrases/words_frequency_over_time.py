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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> words.fig_.write_html("sphinx/_static/analyze/words/abstract_nlp_phrases/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/abstract_nlp_phrases/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| abstract_nlp_phrases         |   2015 |   2016 |   2017 |   2018 |   2019 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|
| FINTECH 32:4952              |      0 |      6 |      5 |      9 |     12 |
| TECHNOLOGIES 23:3317         |      1 |      4 |      4 |      6 |      8 |
| AUTHOR 18:2443               |      0 |      2 |      3 |      6 |      7 |
| FINANCIAL_TECHNOLOGY 17:2225 |      0 |      2 |      1 |      5 |      9 |
| FINANCIAL_INDUSTRY 16:3554   |      0 |      3 |      6 |      5 |      2 |


>>> print(words.prompt_)  # doctest: +ELLIPSIS
Your task is ...






"""
