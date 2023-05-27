"""
Sorts the indicators dataframe by the given metric.

"""


def sort_indicators_by_metric(indicators, metric):
    """
    Sorts the indicators dataframe by the given metric.

    Parameters
    ----------
    indicators : pandas.DataFrame
        Indicators dataframe.

    metric : str
        Metric used to sort the indicators dataframe.

    Returns
    -------
    indicators : pandas.DataFrame
        Indicators dataframe sorted by the given metric.


    """

    indicators = indicators.copy()

    columns = {
        "OCC": ["OCC", "global_citations", "local_citations"],
        "global_citations": ["global_citations", "local_citations", "OCC"],
        "local_citations": ["local_citations", "global_citations", "OCC"],
    }[metric]

    indicators = indicators.sort_values(
        columns, ascending=[False, False, False]
    )

    return indicators
