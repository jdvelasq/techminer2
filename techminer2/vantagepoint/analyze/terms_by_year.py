# flake8: noqa
"""
Terms by Year 
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.terms_by_year(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
... )
>>> r.table_
year                                    2017  2018  2019  ...  2021  2022  2023
author_keywords                                           ...                  
REGTECH 28:329                             2     3     4  ...     3     6     2
FINTECH 12:249                             0     2     4  ...     1     2     0
COMPLIANCE 07:030                          0     0     1  ...     1     1     1
REGULATION 05:164                          0     2     0  ...     1     1     0
FINANCIAL_SERVICES 04:168                  1     1     0  ...     0     1     0
FINANCIAL_REGULATION 04:035                1     0     0  ...     0     2     0
REGULATORY_TECHNOLOGY (REGTECH) 04:030     0     0     0  ...     2     1     0
ARTIFICIAL_INTELLIGENCE 04:023             0     0     1  ...     0     1     0
ANTI_MONEY_LAUNDERING 04:023               0     0     0  ...     3     0     0
RISK_MANAGEMENT 03:014                     0     1     0  ...     0     1     0
<BLANKLINE>
[10 rows x 7 columns]


>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                        |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                         |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249                         |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| COMPLIANCE 07:030                      |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164                      |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| FINANCIAL_SERVICES 04:168              |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINANCIAL_REGULATION 04:035            |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |      0 |      0 |      0 |      1 |      2 |      1 |      0 |
| ARTIFICIAL_INTELLIGENCE 04:023         |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| ANTI_MONEY_LAUNDERING 04:023           |      0 |      0 |      0 |      1 |      3 |      0 |      0 |
| RISK_MANAGEMENT 03:014                 |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
<BLANKLINE>
<BLANKLINE>



>>> r = vantagepoint.analyze.terms_by_year(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
...    cumulative=True,
... )
>>> r.table_
year                                    2017  2018  2019  ...  2021  2022  2023
author_keywords                                           ...                  
REGTECH 28:329                             2     5     9  ...    20    26    28
FINTECH 12:249                             0     2     6  ...    10    12    12
COMPLIANCE 07:030                          0     0     1  ...     5     6     7
REGULATION 05:164                          0     2     2  ...     4     5     5
FINANCIAL_SERVICES 04:168                  1     2     2  ...     3     4     4
FINANCIAL_REGULATION 04:035                1     1     1  ...     2     4     4
REGULATORY_TECHNOLOGY (REGTECH) 04:030     0     0     0  ...     3     4     4
ARTIFICIAL_INTELLIGENCE 04:023             0     0     1  ...     3     4     4
ANTI_MONEY_LAUNDERING 04:023               0     0     0  ...     4     4     4
RISK_MANAGEMENT 03:014                     0     1     1  ...     2     3     3
<BLANKLINE>
[10 rows x 7 columns]


>>> print(r.prompt_)
Analyze the table below which contains the cumulative occurrences by year for the years. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                        |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:---------------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                         |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| FINTECH 12:249                         |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| COMPLIANCE 07:030                      |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| REGULATION 05:164                      |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| FINANCIAL_SERVICES 04:168              |      1 |      2 |      2 |      3 |      3 |      4 |      4 |
| FINANCIAL_REGULATION 04:035            |      1 |      1 |      1 |      2 |      2 |      4 |      4 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |      0 |      0 |      0 |      1 |      3 |      4 |      4 |
| ARTIFICIAL_INTELLIGENCE 04:023         |      0 |      0 |      1 |      3 |      3 |      4 |      4 |
| ANTI_MONEY_LAUNDERING 04:023           |      0 |      0 |      0 |      1 |      4 |      4 |      4 |
| RISK_MANAGEMENT 03:014                 |      0 |      1 |      1 |      2 |      2 |      3 |      3 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...classes import TermsByYear
from ...counters import add_counters_to_axis
from ...item_utils import generate_custom_items
from ...sort_utils import sort_indicators_by_metric
from ...techminer.indicators import indicators_by_field, items_occ_by_year


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
        root_dir (str): Root directory.
        database (str): Database name.
        cumulative (bool, optional): If True, the table contains the cumulative number of occurrences. Defaults to False.
        metric (str): Metric to be used to sort the items.
        top_n (int): Number of top items to be returned.
        occ_range (tuple): Range of occurrence of the items.
        gc_range (tuple): Range of global citations of the items.
        custom_items (list): List of items to be returned.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.


    Returns:
        TermsByYear: A TermsByYear object.


    # pylint: disable=line-too-long
    """

    def generate_prompt(obj):
        return (
            f"Analyze the table below which contains the "
            f"{'cumulative' if obj.cumulative_ else ''} occurrences by year "
            f"for the {obj.criterion_}. Identify any notable "
            "patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a "
            "concise summary of your findings in no more than 150 words."
            f"\n\n{obj.table_.to_markdown()}\n\n"
        )

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
    obj.criterion_ = "years"
    obj.other_criterion_ = field
    obj.cumulative_ = cumulative
    obj.table_ = descriptors_by_year
    obj.prompt_ = generate_prompt(obj)

    return obj
