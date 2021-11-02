"""
Core Sources
===============================================================================




"""

import numpy as np
import pandas as pd

from .utils.explode import explode
from .utils.io import load_records_from_directory


def _core_sources_from_records(records):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    directory_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """
    records = records.copy()

    records["num_documents"] = 1
    records = explode(
        records[
            [
                "publication_name",
                "num_documents",
                "record_id",
            ]
        ],
        "publication_name",
        sep="; ",
    )

    sources = records.groupby("publication_name", as_index=True).agg(
        {
            "num_documents": np.sum,
        }
    )
    sources = sources[["num_documents"]]
    sources = sources.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(sources), 2)) + " %" for a in sources]
    sources = pd.DataFrame(
        {"Num Sources": sources.tolist(), "%": w, "Documents published": sources.index}
    )

    sources = sources.sort_values(["Documents published"], ascending=False)
    sources["Acum Num Sources"] = sources["Num Sources"].cumsum()
    sources["% Acum"] = [
        str(round(100 * a / sum(sources["Num Sources"]), 2)) + " %"
        for a in sources["Acum Num Sources"]
    ]

    sources["Tot Documents published"] = (
        sources["Num Sources"] * sources["Documents published"]
    )
    sources["Num Documents"] = sources["Tot Documents published"].cumsum()
    sources["Tot Documents"] = sources["Num Documents"].map(
        lambda w: str(round(w / sources["Num Documents"].max() * 100, 2)) + " %"
    )

    bradford1 = int(len(records) / 3)
    bradford2 = 2 * bradford1

    sources["Bradford's Group"] = sources["Num Documents"].map(
        lambda w: 3 if w > bradford2 else (2 if w > bradford1 else 1)
    )

    sources = sources[
        [
            "Num Sources",
            "%",
            "Acum Num Sources",
            "% Acum",
            "Documents published",
            "Tot Documents published",
            "Num Documents",
            "Tot Documents",
            "Bradford's Group",
        ]
    ]

    sources = sources.reset_index(drop=True)

    return sources


def _core_sources_from_directory(directory):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    directory: str
        :param directory: path to the directory with the records

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """
    return _core_sources_from_records(load_records_from_directory(directory))


def core_sources(directory_or_records):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    directory_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """
    if isinstance(directory_or_records, str):
        return _core_sources_from_directory(directory_or_records)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _core_sources_from_records(directory_or_records)
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
