# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Word Frequency over Time (Recipe)
===============================================================================

>>> from techminer2.time_analysis import terms_by_year
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
>>> words.fig_.write_html("sphinx/_static/performance_analysis/fields/abstract_nlp_phrases/words_frequency_over_time.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/abstract_nlp_phrases/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| abstract_nlp_phrases           |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_TECHNOLOGY 17:266   |      0 |      2 |      0 |      2 |      6 |      2 |      5 |      0 |
| FINANCIAL_INSTITUTIONS 15:194  |      0 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| REGULATORY_COMPLIANCE 07:198   |      0 |      0 |      2 |      1 |      2 |      1 |      1 |      0 |
| FINANCIAL_SECTOR 07:169        |      0 |      1 |      0 |      0 |      1 |      3 |      2 |      0 |
| ARTIFICIAL_INTELLIGENCE 07:033 |      0 |      0 |      0 |      0 |      3 |      1 |      3 |      0 |

>>> print(words.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'abstract_nlp_phrases' in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| abstract_nlp_phrases           |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGULATORY_TECHNOLOGY 17:266   |      0 |      2 |      0 |      2 |      6 |      2 |      5 |      0 |
| FINANCIAL_INSTITUTIONS 15:194  |      0 |      0 |      2 |      2 |      4 |      3 |      4 |      0 |
| REGULATORY_COMPLIANCE 07:198   |      0 |      0 |      2 |      1 |      2 |      1 |      1 |      0 |
| FINANCIAL_SECTOR 07:169        |      0 |      1 |      0 |      0 |      1 |      3 |      2 |      0 |
| ARTIFICIAL_INTELLIGENCE 07:033 |      0 |      0 |      0 |      0 |      3 |      1 |      3 |      0 |
```
<BLANKLINE>




"""