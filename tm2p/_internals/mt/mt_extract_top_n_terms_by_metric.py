"""
Extracts the top n items (row names) by a metric.

"""


def _mt_extract_top_n_terms_by_metric(
    indicators,
    metric,
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

    from tm2p._internals.mt.mt_sort_records_by_metric import _mt_sort_records_by_metric

    def filter_by_top_n(indicators, top_n):

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
    # 1. Filters the dataframe by OCC y GCS ranges. With this step,
    #    items with very low frequency are ignored.
    if gc_range is not None:
        indicators = filter_by_gc_range(indicators, gc_range)

    if occ_range is not None:
        indicators = filter_by_occ_range(indicators, occ_range)

    #
    # 2. Sort the dataframe by metric.
    indicators = _mt_sort_records_by_metric(indicators, metric)

    #
    # 3. Filters the dataframe by top_n.
    if top_n is not None:
        indicators = filter_by_top_n(indicators, top_n)

    return indicators.index.to_list()
