# flake8: noqa
"""
List View
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"


>>> from techminer2 import vantagepoint
>>> view = vantagepoint.analyze.list_view(
...    field='author_keywords',
...    root_dir=root_dir,
... )
>>> view.table_.head()
                       OCC  ...  local_citations_per_document
author_keywords             ...                              
regtech                 28  ...                          2.64
fintech                 12  ...                          4.08
regulatory technology    7  ...                          2.00
compliance               7  ...                          1.29
regulation               5  ...                          4.40
<BLANKLINE>
[5 rows x 5 columns]



>>> print(view.table_.head().to_markdown())
| author_keywords       |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:----------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech               |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech               |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance            |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation            |     5 |                164 |                22 |                           32.8  |                           4.4  |

>>> print(view.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech                 |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech                 |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology   |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance              |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation              |     5 |                164 |                22 |                           32.8  |                           4.4  |
| financial services      |     4 |                168 |                20 |                           42    |                           5    |
| financial regulation    |     4 |                 35 |                 8 |                            8.75 |                           2    |
| artificial intelligence |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| anti-money laundering   |     3 |                 21 |                 4 |                            7    |                           1.33 |
| risk management         |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""


from ...classes import ListView
from ...item_utils import generate_custom_items
from ...sort_utils import sort_indicators_by_metric
from ...techminer.indicators import indicators_by_item
from ...utils import check_integer, check_integer_range


# pylint: disable=too-many-arguments
def list_view(
    field,
    root_dir="./",
    database="documents",
    metric="OCC",
    # Item filters:
    top_n=10,
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
            "Analyze the table below, which provides bibliometric indicators "
            f"for the field '{field}' in a scientific bibliography database. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
            f"\n\n{table.to_markdown()}\n\n"
        )

    check_integer(top_n)
    check_integer_range(occ_range)
    check_integer_range(gc_range)

    indicators = indicators_by_item(
        field=field,
        root_dir=root_dir,
        database=database,
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
