"""
Source impact table
===============================================================================



>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> source_impact_table(directory=directory).head()
                 num_documents  ...  avg_global_citations
ACCOUNT FINANC               1  ...                 67.00
AM BEHAV SCI                 1  ...                  0.00
ANN OPER RES                 1  ...                  0.00
APPL SCI                     1  ...                  0.00
BANKS BANK SYST              3  ...                  3.33
<BLANKLINE>
[5 rows x 9 columns]



"""
from .impact_indicators import impact_indicators


def source_impact_table(
    directory="./",
):
    sources = impact_indicators(directory=directory, column="iso_source_name")
    sources = sources.sort_index(axis="index", ascending=True)
    return sources
