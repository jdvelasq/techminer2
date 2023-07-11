# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _terms_by_year_table:

Terms by Year Table
===============================================================================

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> tm2.terms_by_year_table(
...     root_dir=root_dir,
...     field="author_keywords",
...     top_n=10,
... )
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


>>> tm2.terms_by_year_table(
...     "author_keywords", 
...     top_n=10, 
...     cumulative=True,
...     root_dir=root_dir,
... )
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



"""
from ...._counters_lib import add_counters_to_frame_axis
from ...._filtering_lib import generate_custom_items
from ...._sorting_lib import sort_indicators_by_metric
from ....techminer.metrics.global_indicators_by_field import (
    global_indicators_by_field,
)
from ....techminer.metrics.items_occurrences_by_year import (
    items_occurrences_by_year,
)


def terms_by_year_table(
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

    descriptors_by_year = items_occurrences_by_year(
        field=field,
        cumulative=cumulative,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_items is None:
        indicators = global_indicators_by_field(
            field=field,
            #
            # DATABASE PARAMS:
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

    descriptors_by_year = add_counters_to_frame_axis(
        descriptors_by_year,
        axis=0,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return descriptors_by_year
