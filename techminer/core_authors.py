"""
Core authors
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> core_authors(directory)
   Num Authors        %  Acum Num Authors   % Acum  \\
0            1   0.03 %                 1   0.03 %   
1            1   0.03 %                 2   0.07 %   
2            3    0.1 %                 5   0.17 %   
3            6    0.2 %                11   0.37 %   
4            8   0.27 %                19   0.65 %   
5           14   0.48 %                33   1.12 %   
6           58   1.97 %                91    3.1 %   
7          246   8.38 %               337  11.47 %   
8         2600  88.53 %              2937  100.0 %   
-
   Documents written per Author  Num Documents % Num Documents  \\
0                            10             10           0.78%   
1                             9              9            0.7%   
2                             7             14           1.09%   
3                             6             30           2.34%   
4                             5             34           2.65%   
5                             4             35           2.73%   
6                             3            103           8.03%   
7                             2            233          18.16%   
8                             1            815          63.52%   
-
   Acum Num Documents % Acum Num Documents  
0                  10                0.78%  
1                  19                1.48%  
2                  33                2.57%  
3                  63                4.91%  
4                  97                7.56%  
5                 132               10.29%  
6                 235               18.32%  
7                 468               36.48%  
8                1283               100.0% 
"""

import pandas as pd

from .column_indicators import column_indicators
from .utils import *


def core_authors(directory):
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
    m = explode(documents[["authors", "document_id"]], "authors", sep="; ")
    m = m.dropna()
    m["Documents_written"] = m.authors.map(lambda w: authors_dict[w])

    n = []
    for k in z["Documents written per Author"]:
        s = m.query("Documents_written >= " + str(k))
        s = s[["document_id"]]
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
