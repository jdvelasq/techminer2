# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Word Frequency over Time
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix/author_keywords/words_frequency_over_time.html"
>>> words = bibliometrix.author_keywords.words_frequency_over_time(
...     top_n=5,
...     root_dir=root_dir,
... )
>>> words.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix/author_keywords/words_frequency_over_time.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(words.df_.to_markdown())
| author_keywords              |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037 |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164            |      0 |      2 |      0 |      1 |      1 |      1 |      0 |

>>> print(words.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'author_keywords' in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords              |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329               |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249               |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037 |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030            |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164            |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
```
<BLANKLINE>





"""
from ...vantagepoint.discover import terms_by_year as analyze_terms_by_year

FIELD = "author_keywords"


def words_frequency_over_time(
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    cumulative=False,
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Makes a dynamics chat for top words."""

    terms_by_year = analyze_terms_by_year(
        field=FIELD,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        cumulative=cumulative,
        **filters,
    )

    return terms_by_year
