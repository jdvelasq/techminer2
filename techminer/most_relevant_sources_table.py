"""
Most relevant sources table
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> most_relevant_sources_table(directory=directory).head()
                 num_documents  global_citations  local_citations
iso_source_name                                                  
ACCOUNT FINANC               1                67                8
AM BEHAV SCI                 1                 0                0
ANN OPER RES                 1                 0                0
APPL SCI                     1                 0                0
BANKS BANK SYST              3                10                3

"""
from .column_indicators import column_indicators


def most_relevant_sources_table(directory="./"):
    sources = column_indicators(directory=directory, column="iso_source_name")
    sources = sources.sort_index(axis="index")
    return sources
