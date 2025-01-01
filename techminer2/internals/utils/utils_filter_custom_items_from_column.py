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


def _utils_filter_custom_items_from_column(dataframe, col_name, custom_items):
    """Filters custom items from a dataframe column."""

    custom_items = [
        item
        for item in custom_items
        if item in dataframe[col_name].drop_duplicates().tolist()
    ]

    return custom_items
