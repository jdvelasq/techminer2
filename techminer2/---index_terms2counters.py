"""
Adds counter to axis
"""

import numpy as np
import pandas as pd

from ._read_records import read_filtered_records
from .explode import explode


def index_terms2counters(
    directory,
    table,
    axis,
    column,
    sep,
):

    documents = read_filtered_records(directory)
    table = table.copy()

    documents = documents.assign(num_documents=1)
    # documents = documents[
    #     [column, "num_documents", "global_citations", "record_no"]
    # ].copy()

    documents = documents[[column, "num_documents", "global_citations"]].copy()

    exploded = explode(documents, column, sep)
    exploded = exploded.groupby(column, as_index=False).agg(
        {
            "num_documents": np.sum,
            "global_citations": np.sum,
        }
    )

    exploded["clean_name"] = exploded[column].copy()
    exploded["clean_name"] = exploded["clean_name"].astype(str)
    # exploded["clean_name"] = exploded["clean_name"].str.replace(r"/\d+", "")

    names = {
        name: (clean_name, ndocs, citations)
        for name, ndocs, citations, clean_name in zip(
            exploded[column],
            exploded["num_documents"],
            exploded["global_citations"],
            exploded["clean_name"],
        )
    }

    if axis in (0, "index"):
        old_names = table.index.tolist()
    if axis in (1, "columns"):
        old_names = table.columns.tolist()

    new_names = [names[current_name] for current_name in old_names]
    new_names = pd.MultiIndex.from_tuples(new_names, names=[column, "#d", "#c"])

    if axis in (0, "index"):
        table.index = new_names
    if axis in (1, "columns"):
        table.columns = new_names

    return table
