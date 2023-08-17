# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Functions for item selection.

"""


def filter_custom_items_from_axis(dataframe, custom_items, axis):
    """Filters custom items from a dataframe axis."""

    if axis == 0:
        topics_list = dataframe.index.tolist()
    else:
        topics_list = dataframe.column.tolist()

    custom_items = [topic for topic in custom_items if topic in topics_list]

    return custom_items


def filter_custom_items_from_column(dataframe, col_name, custom_items):
    """Filters custom items from a dataframe column."""

    custom_items = [
        item for item in custom_items if item in dataframe[col_name].drop_duplicates().tolist()
    ]

    return custom_items


def generate_custom_items(
    indicators,
    metric,
    top_n,
    occ_range,
    gc_range,
    is_trend_analysis,
):
    """Generates custom topics from the index techminer indicators dataframe.

    Args:
        indicators (pandas.DataFrame): a dataframe with the techminer.indicators.
        top_n (int): Number of top items to be returned.
        occ_range (tuple): Range of occurrence of the items.
        gc_range (tuple): Range of global citations of the items.


    Returns:
        A list of items.

    """

    from ._sorting_lib import sort_indicators_by_metric

    def filter_by_top_n(indicators, top_n):
        """Returns the table of indicators filtered by top_n."""

        return indicators.head(top_n)

    def filter_by_occ_range(indicators, occ_range):
        """Returns the table of indicators filtered by occurrence range."""

        if occ_range[0] is not None:
            indicators = indicators[indicators["OCC"] >= occ_range[0]]
        if occ_range[1] is not None:
            indicators = indicators[indicators["OCC"] <= occ_range[1]]
        return indicators

    def filter_by_gc_range(indicators, gc_range):
        """Returns the table of indicators filtered by global citations range."""

        if gc_range[0] is not None:
            indicators = indicators[indicators["global_citations"] >= gc_range[0]]
        if gc_range[1] is not None:
            indicators = indicators[indicators["global_citations"] <= gc_range[1]]
        return indicators

    #
    # Main code:
    #
    # This is a complex filter for the indicators dataframe. It is based on
    # the requirements of ScientoPy for calculating the top trending items.
    #

    #
    # 1. Filters the dataframe by OCC y GCS ranges.
    #    With this step, items with very low frequency are ignored.
    if gc_range is not None:
        indicators = filter_by_gc_range(indicators, gc_range)

    if occ_range is not None:
        indicators = filter_by_occ_range(indicators, occ_range)

    #
    # 2. In trend analysis, the dataframe is sorted by the AGR;
    #    otherwise, it is sorted by the metric.
    if is_trend_analysis:
        indicators = sort_indicators_by_metric(
            indicators, "average_growth_rate", is_trend_analysis=True
        )
    else:
        indicators = sort_indicators_by_metric(indicators, metric, is_trend_analysis=False)

    #
    # 3. Filters the dataframe by top_n.
    if top_n is not None:
        indicators = filter_by_top_n(indicators, top_n)

    return indicators.index.to_list()
