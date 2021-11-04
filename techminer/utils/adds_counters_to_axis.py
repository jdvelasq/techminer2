"""
Adds counter to axis
"""

import numpy as np
import pandas as pd

from .explode import explode
from .io import load_documents


def _adds_counters_to_axis_from_records(
    records,
    table,
    axis,
    column,
    sep,
):

    table = table.copy()
    records = records.copy()

    records = records.assign(num_documents=1)
    records = records[[column, "num_documents", "global_citations", "record_id"]].copy()

    exploded = explode(records, column, sep)
    exploded = exploded.groupby(column, as_index=False).agg(
        {
            "num_documents": np.sum,
            "global_citations": np.sum,
        }
    )

    names = {
        name: (name, ndocs, citations)
        for name, ndocs, citations in zip(
            exploded[column], exploded["num_documents"], exploded["global_citations"]
        )
    }

    if axis in (0, "index"):
        old_names = table.index.tolist()
    if axis in (1, "columns"):
        old_names = table.columns.tolist()

    new_names = [names[current_name] for current_name in old_names]
    new_names = pd.MultiIndex.from_tuples(
        new_names, names=[column, "num_docs", "cited_by"]
    )

    if axis in (0, "index"):
        table.index = new_names
    if axis in (1, "columns"):
        table.columns = new_names

    return table


def _adds_counters_to_axis_from_directory(
    directory,
    table,
    axis,
    column,
    sep,
):
    return _adds_counters_to_axis_from_records(
        records=load_documents(directory),
        table=table,
        axis=axis,
        column=column,
        sep=sep,
    )


def adds_counters_to_axis(
    directory_or_records,
    table,
    axis,
    column,
    sep,
):
    """
    Adds counters to axis.
    """
    if isinstance(directory_or_records, str):
        return _adds_counters_to_axis_from_directory(
            directory=load_records_from_project_directory(directory_or_records),
            table=table,
            axis=axis,
            column=column,
            sep=sep,
        )
    if isinstance(directory_or_records, pd.DataFrame):
        return _adds_counters_to_axis_from_records(
            records=directory_or_records,
            table=table,
            axis=axis,
            column=column,
            sep=sep,
        )
    raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
