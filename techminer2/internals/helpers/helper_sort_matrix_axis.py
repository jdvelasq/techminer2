# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Sorts matrix axis.

"""


def helper_sort_matrix_axis(
    matrix,
    axis,
    field,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Sorts the axis of the matrix by 'OCC', 'global_citations', and 'local_citations'."""

    from ..._core.metrics.calculate_global_performance_metrics import (
        calculate_global_performance_metrics,
    )
    from ..._core.metrics.sort_records_by_metric import sort_records_by_metric

    matrix = matrix.copy()

    indicators_by_topic = calculate_global_performance_metrics(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators_by_topic = sort_records_by_metric(
        indicators_by_topic,
        "OCC",
    )

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
