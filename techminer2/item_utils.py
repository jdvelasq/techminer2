# flake8: noqa
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
        item
        for item in custom_items
        if item in dataframe[col_name].drop_duplicates().tolist()
    ]

    return custom_items


def generate_custom_items(
    indicators,
    top_n,
    occ_range,
    gc_range,
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

    def filter_by_top_n(indicators, top_n):
        return indicators.index[:top_n].tolist()

    def filter_by_occ_range(indicators, occ_range):
        return indicators[
            (indicators["OCC"] >= occ_range[0])
            & (indicators["OCC"] <= occ_range[1])
        ].index.tolist()

    def filter_by_gc_range(indicators, gc_range):
        return indicators[
            (indicators["global_citations"] >= gc_range[0])
            & (indicators["global_citations"] <= gc_range[1])
        ].index.tolist()

    #
    # Main code
    #

    if top_n is not None:
        return filter_by_top_n(indicators, top_n)

    if occ_range is not None:
        return filter_by_occ_range(indicators, occ_range)

    if gc_range is not None:
        return filter_by_gc_range(indicators, gc_range)

    return indicators.index.tolist()
