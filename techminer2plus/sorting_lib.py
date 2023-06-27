# flake8: noqa
"""
Sorts the indicators dataframe by the given metric.

"""


def sort_indicators_by_metric(indicators, metric):
    """
    Sorts the indicators dataframe by the given metric.


    """

    indicators = indicators.copy()
    indicators["_name_"] = indicators.index.tolist()

    columns = {
        # -------------------------------------------
        "OCCGC": [
            "OCC",
            "global_citations",
            "local_citations",
            "_name_",
        ],
        # -------------------------------------------
        "OCC": [
            "OCC",
            "global_citations",
            "local_citations",
            "_name_",
        ],
        # -------------------------------------------
        "global_citations": [
            "global_citations",
            "local_citations",
            "OCC",
            "_name_",
        ],
        # -------------------------------------------
        "local_citations": [
            "local_citations",
            "global_citations",
            "OCC",
            "_name_",
        ],
        # -------------------------------------------
        "h_index": [
            "h_index",
            "global_citations",
            "OCC",
            "_name_",
        ],
        # -------------------------------------------
        "g_index": [
            "g_index",
            "global_citations",
            "OCC",
            "_name_",
        ],
        # -------------------------------------------
        "m_index": [
            "m_index",
            "global_citations",
            "OCC",
            "_name_",
        ],
        # -------------------------------------------
    }[metric]

    indicators = indicators.sort_values(
        columns, ascending=[False, False, False, True]
    )

    indicators = indicators.drop(columns=["_name_"])

    return indicators


# pylint: disable=import-outside-toplevel
def sort_matrix_axis(
    matrix,
    axis,
    field,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Sorts the axis of the matrix by 'OCC', 'global_citations', and 'local_citations'.

    # pylint: disable=line-too-long
    """

    from .metrics_lib.indicators_by_field import indicators_by_field

    matrix = matrix.copy()

    indicators_by_topic = indicators_by_field(
        field=field,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
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
