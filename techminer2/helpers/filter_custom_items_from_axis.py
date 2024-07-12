# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
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
