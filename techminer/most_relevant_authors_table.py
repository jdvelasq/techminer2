"""
Most relevant authors table
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> most_relevant_authors_table(directory=directory).head()
               num_documents  global_citations  local_citations
authors                                                        
Aas TH                     1                 0                0
Abakah EJA                 1                17                1
Abbas F                    1                 5                2
Abdullah EME               1                 8                1
Abu Daqar MAM              1                 2                2

"""
import matplotlib.pyplot as plt

from .column_indicators import column_indicators


def most_relevant_authors_table(
    directory="./",
):
    authors = column_indicators(directory=directory, column="authors")
    authors = authors.sort_index(axis="index")

    return authors
