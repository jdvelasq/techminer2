"""
Core authors
===============================================================================

>>> from techminer import core_authors
>>> directory = "/workspaces/techminer-api/data/"
>>> core_authors(directory)
   Num Authors       %  ...  Acum Num Documents % Acum Num Documents
0            1  0.05 %  ...                   8                0.99%
1            1  0.05 %  ...                  15                1.86%
2            2  0.11 %  ...                  21                 2.6%
3            6  0.32 %  ...                  46                 5.7%
4            9  0.49 %  ...                  72                8.92%
5           36  1.95 %  ...                 133               16.48%
6          128  6.92 %  ...                 265               32.84%
7         1666  90.1 %  ...                 807               100.0%
<BLANKLINE>
[8 rows x 9 columns]

"""

import pandas as pd

from .column_indicators import column_indicators
from .utils import *


def core_authors(directory="./"):
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
    documents = load_filtered_documents(directory)
    documents = documents.copy()

    z = column_indicators(directory, "authors", sep="; ")["num_documents"]

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
    m = explode(documents[["authors", "record_no"]], "authors", sep="; ")
    m = m.dropna()
    m["Documents_written"] = m.authors.map(lambda w: authors_dict[w])

    n = []
    for k in z["Documents written per Author"]:
        s = m.query("Documents_written >= " + str(k))
        s = s[["record_no"]]
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
