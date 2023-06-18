# flake8: noqa
"""
Terms by Year 
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> r = techminer2plus.system.analyze.terms_by_year(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
... )
>>> r.table_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     3     4     8     3     6     2
FINTECH 12:249                     0     2     4     3     1     2     0
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     3     2     0
COMPLIANCE 07:030                  0     0     1     3     1     1     1
REGULATION 05:164                  0     2     0     1     1     1     0
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     3     0     0
FINANCIAL_SERVICES 04:168          1     1     0     1     0     1     0
FINANCIAL_REGULATION 04:035        1     0     0     1     0     2     0
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     2     0     1     0
RISK_MANAGEMENT 03:014             0     1     0     1     0     1     0



>>> print(r.prompt_)
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





>>> r = techminer2plus.system.analyze.terms_by_year(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
...    cumulative=True,
... )
>>> r.table_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     5     9    17    20    26    28
FINTECH 12:249                     0     2     6     9    10    12    12
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     5     7     7
COMPLIANCE 07:030                  0     0     1     4     5     6     7
REGULATION 05:164                  0     2     2     3     4     5     5
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     5     5     5
FINANCIAL_SERVICES 04:168          1     2     2     3     3     4     4
FINANCIAL_REGULATION 04:035        1     1     1     2     2     4     4
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     3     3     4     4
RISK_MANAGEMENT 03:014             0     1     1     2     2     3     3

>>> print(r.prompt_)
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


# pylint: disable=line-too-long
"""
# import textwrap

# from ..classes import TermsByYear
# from ..counters import add_counters_to_axis
# from ..indicators import indicators_by_field, items_occ_by_year
# from ..items import generate_custom_items
# from ..prompts import format_prompt_for_tables
# from ..sorting import sort_indicators_by_metric


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def terms_by_year(
    field,
    # Table params:
    cumulative=False,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes a table with the number of occurrences of each term by year.

    Args:
        field (str): Database field to be used to extract the items.
        cumulative (bool, optional): If True, the table contains the cumulative number of occurrences. Defaults to False.

        top_n (int): Number of top items to be returned.
        occ_range (tuple): Range of occurrence of the items.
        gc_range (tuple): Range of global citations of the items.
        custom_items (list): List of items to be returned.

        root_dir (str): Root directory.
        database (str): Database name.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.


    Returns:
        TermsByYear: A TermsByYear object.


    # pylint: disable=line-too-long
    """

    def generate_prompt(obj):
        # pylint: disable=line-too-long
        main_text = (
            "Your task is to generate an analysis about the "
            f"{'cumulative' if obj.cumulative_ else ''} occurrences by year "
            f"of the '{obj.field_}' in a scientific bibliography database. "
            "Summarize the table below, delimited by triple backticks, "
            "identify any notable patterns, trends, or outliers in the data, "
            "and disc  uss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
        )
        return format_prompt_for_tables(main_text, obj.table_.to_markdown())

    #
    # Main:
    #

    descriptors_by_year = items_occ_by_year(
        field=field,
        root_dir=root_dir,
        cumulative=cumulative,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_items is None:
        indicators = indicators_by_field(
            field=field,
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        indicators = sort_indicators_by_metric(indicators, metric="OCC")

        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    descriptors_by_year = descriptors_by_year[
        descriptors_by_year.index.isin(custom_items)
    ]

    descriptors_by_year = descriptors_by_year.loc[custom_items, :]

    descriptors_by_year = add_counters_to_axis(
        descriptors_by_year,
        axis=0,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj = TermsByYear()
    obj.metric_ = "OCC"
    obj.field_ = field
    obj.cumulative_ = cumulative
    obj.table_ = descriptors_by_year
    obj.prompt_ = generate_prompt(obj)

    return obj
