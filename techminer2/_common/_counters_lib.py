# flake8: noqa
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
"""
This module implements functions to add OCC:citations counters to topics 
in the values or axis of a dataframe.




"""

import numpy as np

from ..core.calculate_global_performance_metrics import (
    calculate_global_performance_metrics,
)


def add_counters_to_frame_axis(
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

    new_column_names = items2counters(
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


def add_counters_to_column_values(
    criterion,
    table,
    name,
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """:meta private:"""
    new_column_names = items2counters(
        criterion=criterion,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    table[name] = table[name].map(new_column_names)
    return table


def items2counters(
    criterion,
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """Creates a dictionary to transform a 'item' to a 'item counter:counter'."""

    indicators = calculate_global_performance_metrics(
        field=criterion,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    names = indicators.index.to_list()
    occ = indicators.OCC.to_list()
    cited_by = indicators.global_citations.to_list()

    n_zeros_occ = int(np.log10(max(occ))) + 1
    n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

    fmt_occ = "{:0" + str(n_zeros_occ) + "d}"
    fmt_cited_by = "{:0" + str(n_zeros_cited_by) + "d}"
    fmt = "{} " + f"{fmt_occ}:{fmt_cited_by}"

    return {
        name: fmt.format(name, int(nd), int(tc))
        for name, nd, tc in zip(names, occ, cited_by)
    }


def remove_counters_from_axis(
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
