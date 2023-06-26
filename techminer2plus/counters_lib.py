# flake8: noqa
"""
This module implements functions to add OCC:citations counters to topics 
in the values or axis of a dataframe.



# pylint: disable=line-too-long
"""

import numpy as np

from .metrics import indicators_by_field


# pylint: disable=too-many-arguments
def add_counters_to_axis(
    dataframe,
    axis,
    field,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Adds OCC:citations counters to topics in the axis of a dataframe.

    Args:
        dataframe (pandas.DataFrame): The dataframe.
        axis (int): 0 for index, 1 for columns.
        criterion (str): The criterion to be analyzed.
        root_dir (str): The working directory.
        database (str): The database name. It can be 'documents', 'cited_by' or 'references'.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.


    Returns:
        pandas.DataFrame: The dataframe with OCC:citations counters added to topics in the axis.

    """

    dataframe = dataframe.copy()

    new_column_names = items2counters(
        criterion=field,
        root_dir=root_dir,
        database=database,
        start_year=year_filter,
        end_year=cited_by_filter,
        **filters,
    )

    if axis == 0:
        dataframe.index = dataframe.index.map(new_column_names)
    else:
        dataframe.columns = dataframe.columns.map(new_column_names)

    return dataframe


def add_counters_to_column_values(
    criterion,
    name,
    root_dir,
    database,
    table,
    start_year,
    end_year,
    **filters,
):
    new_column_names = items2counters(
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    table[name] = table[name].map(new_column_names)
    return table


def items2counters(
    criterion,
    root_dir,
    database,
    start_year,
    end_year,
    **filters,
):
    """Creates a dictionary to transform a 'item' to a 'item counter:counter'."""

    indicators = indicators_by_field(
        field=criterion,
        root_dir=root_dir,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
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
