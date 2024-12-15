# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Sorts the indicators dataframe by the given metric.

"""

SELECTED_COLUMNS = {
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
}


def sort_records_by_metric(
    indicators,
    metric,
):
    """
    Sorts the indicators dataframe by the given metric.
    """

    indicators = indicators.copy()
    indicators["_name_"] = indicators.index.tolist()

    columns = SELECTED_COLUMNS[metric]
    ascending = [False] * (len(columns) - 1) + [True]

    indicators = indicators.sort_values(columns, ascending=ascending)
    indicators = indicators.drop(columns=["_name_"])

    return indicators
