# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Word Frequency over Time
===============================================================================

>>> from techminer2.analyze import terms_by_year
>>> words = terms_by_year(
...     #
...     # PARAMS:
...     field="words",
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
>>> words.fig_.write_html("sphinx/_static/analyze/words/words/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/words/words/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown()) # doctest: +ELLIPSIS
| words ...



>>> print(words.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
