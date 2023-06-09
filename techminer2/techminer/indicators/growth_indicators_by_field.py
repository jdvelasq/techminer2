# flake8: noqa
"""
Growth Indicators by Field
===============================================================================

TechMiner2 computes three growth indicators for each item in a field (usually
keywords or noun phrases):

* Average growth rate (AGR):

.. code-block::

           sum_{i=Y_start}^Y_end  Num_Documents[i] - Num_Documents[i-1]
    AGR = --------------------------------------------------------------
                            Y_end - Y_start + 1


* Average documents per year (ADY):

.. code-block::

           sum_{i=Y_start}^Y_end  Num_Documents[i]
    ADY = -----------------------------------------
                    Y_end - Y_start + 1


* Percentage of documents in last year (PDLY):

.. code-block::

           sum_{i=Y_start}^Y_end  Num_Documents[i]      1
    PDLY = ---------------------------------------- * _____
                  Y_end - Y_start + 1                  TND


With:

.. code-block::

    Y_start = Y_end - time_window + 1



    
If ``Y_end = 2018`` and ``time_window = 2``, then ``Y_start = 2017``.



Examples
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import techminer
>>> custom_items = ['REGTECH', 'FINTECH', 'COMPLIANCE', 'REGULATION', 
...     'ARTIFICIAL_INTELLIGENCE']
>>> items_occ_by_year(
...     field="author_keywords",
...     root_dir=root_dir,
... ).loc[custom_items, :]
year                     2017  2018  2019  2020  2021  2022  2023
author_keywords                                                  
REGTECH                     2     3     4     8     3     6     2
FINTECH                     0     2     4     3     1     2     0
COMPLIANCE                  0     0     1     3     1     1     1
REGULATION                  0     2     0     1     1     1     0
ARTIFICIAL_INTELLIGENCE     0     0     1     2     0     1     0


>>> from techminer2 import techminer
>>> indicators = techminer.indicators.growth_indicators_by_field(
...     field="author_keywords",
...     root_dir=root_dir,
... )
>>> print(indicators.head().to_markdown())
| author_keywords         |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_of_docs_in_last_years |
|:------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------------------------:|
| REGTECH                 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                          0.142857  |
| FINTECH                 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                          0.0833333 |
| COMPLIANCE              |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                          0.142857  |
| REGULATION              |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                          0.1       |
| ARTIFICIAL_INTELLIGENCE |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                          0.125     |

# pylint: disable=line-too-long
"""
from .indicators_by_field import indicators_by_field
from .items_occ_by_year import items_occ_by_year


# pylint: disable=too-many-arguments
def growth_indicators_by_field(
    field,
    # Specific params:
    time_window=2,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes growth indicators."""

    # computes the occurrences of each item in each year
    items_by_year = items_occ_by_year(
        field=field,
        cumulative=False,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators_by_field(
        field=field,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # creates a dataframe with the OCC per item
    tnd = indicators["OCC"].copy()

    # computes the range of years
    year_end = items_by_year.columns.max()
    year_start = year_end - time_window + 1
    year_columns = list(range(year_start - 1, year_end + 1))

    # computes the number of documents per period by item
    between = f"Between {year_start}-{year_end}"
    before = f"Before {year_start}"
    indicators[between] = items_by_year.loc[:, year_columns[1:]].sum(axis=1)
    indicators[before] = indicators["OCC"] - indicators[between]

    # sort the columns
    columns = ["OCC", before, between] + [
        col
        for col in indicators.columns
        if col not in ["OCC", before, between]
    ]
    indicators = indicators[columns]

    # selects the columns of interest
    items_by_year = items_by_year.loc[:, year_columns]

    # agr: average growth rate
    agr = items_by_year.diff(axis=1)
    agr = agr.loc[:, year_columns[1:]]
    agr = agr.sum(axis=1) / time_window

    # ady: average documents per year
    ady = items_by_year.loc[:, year_columns[1:]].sum(axis=1) / time_window

    # pdly: percentage of documents in last year
    pdly = ady / tnd

    # Completes the indicators:
    indicators["average_growth_rate"] = agr
    indicators["average_docs_per_year"] = ady
    indicators["percentage_of_docs_in_last_years"] = pdly

    indicators = indicators.dropna()
    indicators["_name_"] = indicators.index
    indicators = indicators.sort_values(
        ["OCC", "average_growth_rate", "_name_"],
        ascending=[False, False, True],
    )
    indicators = indicators.drop(columns=["_name_"])
    return indicators
