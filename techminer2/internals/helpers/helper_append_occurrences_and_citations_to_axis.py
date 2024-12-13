# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
"""
This module implements functions to add OCC:citations counters to topics 
in the values or axis of a dataframe.




"""
from .helper_compute_occurrences_and_citations import (
    helper_compute_occurrences_and_citations,
)


def helper_append_occurrences_and_citations_to_axis(
    dataframe,
    axis,
    field,
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """:meta private:"""

    dataframe = dataframe.copy()

    new_column_names = helper_compute_occurrences_and_citations(
        criterion=field,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if axis == 0:
        dataframe.index = dataframe.index.map(new_column_names)
    else:
        dataframe.columns = dataframe.columns.map(new_column_names)

    return dataframe
