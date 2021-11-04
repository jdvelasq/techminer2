"""
Core Authors
===============================================================================
"""

import pandas as pd

from techminer.terms_table import count_records_by_term

from .utils import *


def _core_authors_from_records(records):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core authors of the records
    """
    records = records.copy()

    z = count_records_by_term(records, "authors", sep="; ")

    authors_dict = {
        author: num_docs for author, num_docs in zip(z.index, z) if not pd.isna(author)
    }

    #
    #  Num Authors x Documents written per Author
    #
    # z = z[["num_documents"]]
    z = z.to_frame(name="num_documents")
    z = z.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(z), 2)) + " %" for a in z]
    z = pd.DataFrame(
        {"Num Authors": z.tolist(), "%": w, "Documents written per Author": z.index}
    )
    z = z.sort_values(["Documents written per Author"], ascending=False)
    z["Acum Num Authors"] = z["Num Authors"].cumsum()
    z["% Acum"] = [
        str(round(100 * a / sum(z["Num Authors"]), 2)) + " %"
        for a in z["Acum Num Authors"]
    ]
    m = explode(records[["authors", "record_id"]], "authors", sep="; ")
    m = m.dropna()
    m["Documents_written"] = m.authors.map(lambda w: authors_dict[w])

    n = []
    for k in z["Documents written per Author"]:
        s = m.query("Documents_written >= " + str(k))
        s = s[["record_id"]]
        s = s.drop_duplicates()
        n.append(len(s))

    k = []
    for index in range(len(n) - 1):
        k.append(n[index + 1] - n[index])
    k = [n[0]] + k
    z["Num Documents"] = k
    z["% Num Documents"] = [str(round(i / max(n) * 100, 2)) + "%" for i in k]
    z["Acum Num Documents"] = n
    z["% Acum Num Documents"] = [str(round(i / max(n) * 100, 2)) + "%" for i in n]

    z = z[
        [
            "Num Authors",
            "%",
            "Acum Num Authors",
            "% Acum",
            "Documents written per Author",
            "Num Documents",
            "% Num Documents",
            "Acum Num Documents",
            "% Acum Num Documents",
        ]
    ]

    return z.reset_index(drop=True)


def _core_authors_from_directory(directory):
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
    return _core_authors_from_records(load_records_from_directory(directory))


def core_authors(dirpath_or_records):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core authors of the records
    """
    if isinstance(dirpath_or_records, str):
        return _core_authors_from_directory(dirpath_or_records)
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _core_authors_from_records(dirpath_or_records)
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")
