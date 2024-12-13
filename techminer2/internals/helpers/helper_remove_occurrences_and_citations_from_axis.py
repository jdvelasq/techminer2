# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
"""
This module implements




"""


def helper_remove_occurrences_and_citations_from_axis(
    dataframe,
    axis,
):
    """Remove counters from axis."""

    def remove_counters(text):
        text = text.split(" ")
        text = text[:-1]
        text = " ".join(text)
        return text

    dataframe = dataframe.copy()

    if axis == 0:
        dataframe.index = dataframe.index.map(remove_counters)
    else:
        dataframe.columns = dataframe.columns.map(remove_counters)

    return dataframe
