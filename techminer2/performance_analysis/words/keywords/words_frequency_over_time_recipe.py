# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Word Frequency over Time (Recipe)
===============================================================================

>>> from techminer2.performance_analysis import terms_by_year
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> words.fig_.write_html("sphinx/_static/performance_analysis/fields/keywords/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| keywords                     |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_COMPLIANCE 09:034 |      1 |      0 |      1 |      3 |      1 |      2 |      1 |
| REGULATORY_TECHNOLOGY 08:037 |      0 |      0 |      0 |      2 |      3 |      2 |      1 |
| COMPLIANCE 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |


>>> print(words.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'keywords' in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| keywords                     |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_COMPLIANCE 09:034 |      1 |      0 |      1 |      3 |      1 |      2 |      1 |
| REGULATORY_TECHNOLOGY 08:037 |      0 |      0 |      0 |      2 |      3 |      2 |      1 |
| COMPLIANCE 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
```
<BLANKLINE>

"""
