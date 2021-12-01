"""
Most local cited sources table
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> most_local_cited_sources_table(directory=directory).head()
                           local_citations
iso_source_name                           
ELECT COMMER RES APPL                   90
MIS QUART MANAGE INF SYST               76
REV FINANC STUD                         75
J MANAGE INF SYST                       73
J FINANC ECON                           72

"""
from os.path import join

import matplotlib.pyplot as plt
import pandas as pd

from .column_indicators import column_indicators


def most_local_cited_sources_table(directory="./"):

    references = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    references = references[["iso_source_name", "local_citations"]]
    references = references.groupby("iso_source_name").sum()
    references = references.sort_values(by="local_citations", ascending=False)
    return references
