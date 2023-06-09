"""ScientoPy common functions. """

from ..item_utils import generate_custom_items
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators.growth_indicators_by_field import (
    growth_indicators_by_field,
)

PROMPT = """\
Your task is to generate a short analysis for a scientific research paper. \
Analyze the table below, delimited by triple backticks, in at most {n_words} \
words, for the different items of the field '{field}', providing conclusions \
about the different columns of the table, and take into account that the \
columns {before} and {between} represents the number of documents for each \
item in the indicated time period.
"""


def get_default_indicators(
    field,
    # Specific params:
    time_window,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    # compute growth indicators for all items in the database
    indicators = growth_indicators_by_field(
        field=field,
        time_window=time_window,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # sort the indicators "as usual" for the selection phase
    indicators = sort_indicators_by_metric(indicators, "OCC")

    # filter the items
    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )
    indicators = indicators[indicators.index.isin(custom_items)]

    #
    columns = ["OCC", "global_citations", "average_growth_rate", "_name_"]
    indicators["_name_"] = indicators.index
    indicators = indicators.sort_values(
        by=columns,
        ascending=[False, False, False, True],
    )
    indicators = indicators.drop(columns=["_name_"])

    return indicators


def get_trend_indicators(
    field,
    # Specific params:
    time_window,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    # compute growth indicators for all items in the database
    indicators = growth_indicators_by_field(
        field=field,
        time_window=time_window,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # sort the indicators "as usual" for the selection phase
    indicators = sort_indicators_by_metric(indicators, "OCC")

    if custom_items is None:
        #
        # This phase differes of the rest of the tools:
        # 1. Apply the filters
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=None,
            occ_range=occ_range,
            gc_range=gc_range,
        )

        # 2. Selects the all the items in the filtered range of data
        indicators = indicators[indicators.index.isin(custom_items)]

        # 2. Sorts the indicators by the average growth rate
        columns = ["average_growth_rate", "OCC", "global_citations", "_name_"]
        indicators["_name_"] = indicators.index
        indicators = indicators.sort_values(
            by=columns,
            ascending=[False, False, False, True],
        )
        indicators = indicators.drop(columns=["_name_"])

        # 3. select the top_n items
        if top_n is not None:
            indicators = indicators.head(top_n)

    else:
        # The user suministrate a list of items.
        # Only sorts the data.
        columns = ["average_growth_rate", "OCC", "global_citations", "_name_"]
        indicators["_name_"] = indicators.index
        indicators = indicators.sort_values(
            by=columns,
            ascending=[False, False, False, True],
        )
        indicators = indicators.drop(columns=["_name_"])
        indicators = indicators[indicators.index.isin(custom_items)]

    return indicators


#
