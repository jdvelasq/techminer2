"""
Most local cited authors table
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> most_local_cited_authors_table(directory=directory).head()
                local_citations
authors                        
(Chad) Ho Y-C                 3
@ Mat Isa MPBM                1
A Asongu S                    9
Aaker DA                      1
Aamir N                       1


"""
from os.path import join

import matplotlib.pyplot as plt
import pandas as pd

from .column_indicators import column_indicators


def most_local_cited_authors_table(directory="./"):

    references = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    references = references[["authors", "local_citations"]]
    references = references.dropna()
    references = references.assign(authors=references.authors.str.split(";"))
    references = references.explode("authors")
    references = references.assign(authors=references.authors.str.strip())
    references = references.groupby("authors").sum()
    references = references.sort_index(axis="index")
    return references
