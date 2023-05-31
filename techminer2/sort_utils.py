"""
Sorts the indicators dataframe by the given metric.

"""

from . import techminer


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
    indicators["name"] = indicators.index.tolist()

    columns = {
        "OCC": ["OCC", "global_citations", "local_citations", "name"],
        "global_citations": [
            "global_citations",
            "local_citations",
            "OCC",
            "name",
        ],
        "local_citations": [
            "local_citations",
            "global_citations",
            "OCC",
            "name",
        ],
    }[metric]

    indicators = indicators.sort_values(
        columns, ascending=[False, False, False, True]
    )

    indicators = indicators.drop(columns=["name"])

    return indicators


def sort_matrix_axis(
    matrix,
    axis,
    criterion,
    root_dir,
    database,
    start_year,
    end_year,
    **filters,
):
    """Sorts the axis of the matrix by 'OCC', 'global_citations', and 'local_citations'."""

    matrix = matrix.copy()

    indicators_by_topic = techminer.indicators.indicators_by_topic(
        field=criterion,
        root_dir=root_dir,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    indicators_by_topic = sort_indicators_by_metric(indicators_by_topic, "OCC")

    if axis == 0:
        topics = [
            topic
            for topic in indicators_by_topic.index.tolist()
            if topic in matrix.index.tolist()
        ]
        matrix = matrix.loc[topics, :]
    else:
        topics = [
            topic
            for topic in indicators_by_topic.index.tolist()
            if topic in matrix.columns.tolist()
        ]
        matrix = matrix.loc[:, topics]

    return matrix
