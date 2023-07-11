# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _terms_by_year_prompt:

Terms by Year Prompt
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.terms_by_year_prompt(
...     root_dir=root_dir,
...     field="author_keywords",
...     top_n=10,
... )
>>> print(prompt)
Your task is to generate an analysis about the  occurrences by year of the \\
'author_keywords' in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249                 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164              |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      3 |      0 |      0 |
| FINANCIAL_SERVICES 04:168      |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINANCIAL_REGULATION 04:035    |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
```
<BLANKLINE>




>>> prompt = tm2p.terms_by_year_prompt(
...     "author_keywords", 
...     top_n=10, 
...     cumulative=True,
...     root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate an analysis about the cumulative occurrences by \\
year of the 'author_keywords' in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, identify any \\
notable patterns, trends, or outliers in the data, and disc  uss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| FINTECH 12:249                 |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      5 |      7 |      7 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| REGULATION 05:164              |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      5 |      5 |      5 |
| FINANCIAL_SERVICES 04:168      |      1 |      2 |      2 |      3 |      3 |      4 |      4 |
| FINANCIAL_REGULATION 04:035    |      1 |      1 |      1 |      2 |      2 |      4 |      4 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      3 |      3 |      4 |      4 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      1 |      2 |      2 |      3 |      3 |
```
<BLANKLINE>



"""
from .format_prompt_for_dataframes import format_prompt_for_dataframes
from .terms_by_year_table import terms_by_year_table


def terms_by_year_prompt(
    #
    # PARAMS:
    field,
    cumulative=False,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    # pylint: disable=line-too-long
    """Computes a table with the number of occurrences of each term by year."""

    data_frame = terms_by_year_table(
        #
        # PARAMS:
        field=field,
        cumulative=cumulative,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    main_text = (
        "Your task is to generate an analysis about the "
        f"{'cumulative' if cumulative else ''} occurrences by year "
        f"of the '{field}' in a scientific bibliography database. "
        "Summarize the table below, delimited by triple backticks, "
        "identify any notable patterns, trends, or outliers in the data, "
        "and disc  uss their implications for the research field. Be sure "
        "to provide a concise summary of your findings in no more than "
        "150 words."
    )

    return format_prompt_for_dataframes(main_text, data_frame.to_markdown())
