# flake8: noqa
"""
Impact View (*)
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"


>>> from techminer2 import vantagepoint
>>> view = vantagepoint.analyze.impact_view(
...    field='authors',
...    root_dir=root_dir,
... )
>>> view.table_.head()
             OCC  ...  avg_global_citations
authors           ...                      
Arner DW       3  ...                 61.67
Buckley RP     3  ...                 61.67
Barberis JN    2  ...                 80.50
Butler T/1     2  ...                 20.50
Hamdan A       2  ...                  9.00
<BLANKLINE>
[5 rows x 9 columns]


>>> print(view.table_.head().to_markdown())
| authors     |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Arner DW    |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Buckley RP  |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Barberis JN |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
| Butler T/1  |     2 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  20.5  |
| Hamdan A    |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |


>>> print(view.prompt_)
Analyze the table below, which provides impact indicators for the field 'authors' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors     |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Arner DW    |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Buckley RP  |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Barberis JN |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
| Butler T/1  |     2 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  20.5  |
| Hamdan A    |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
| Turki M     |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
| Lin W       |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Singh C     |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Brennan R   |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Crane M     |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""


from ...check_params import (
    check_impact_metric,
    check_integer,
    check_integer_range,
)
from ...classes import ListView
from ...item_utils import generate_custom_items
from ...sort_utils import sort_indicators_by_metric
from ...techminer.indicators import impact_indicators_by_field


# pylint: disable=too-many-arguments
def impact_view(
    field,
    root_dir="./",
    database="documents",
    metric="h_index",
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Returns a dataframe with the extracted items.

    Args:
        field (str): Database field to be used to extract the items.
        root_dir (str): Root directory.
        database (str): Database name.
        metric (str): Metric to be used to sort the items.
        top_n (int): Number of top items to be returned.
        occ_range (tuple): Range of occurrence of the items.
        gc_range (tuple): Range of global citations of the items.
        custom_items (list): List of items to be returned.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        A ListView object.

    """

    def generate_prompt(field, table):
        return (
            "Analyze the table below, which provides impact indicators "
            f"for the field '{field}' in a scientific bibliography database. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
            f"\n\n{table.to_markdown()}\n\n"
        )

    check_impact_metric(metric)
    check_integer_range(gc_range)
    check_integer_range(occ_range)
    check_integer(top_n)

    indicators = impact_indicators_by_field(
        field=field,
        root_dir=root_dir,
        database=database,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, metric)

    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    results = ListView()
    results.table_ = indicators
    results.prompt_ = generate_prompt(field, indicators)
    results.metric_ = metric
    results.field_ = field

    return results
