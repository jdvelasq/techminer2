"""
Co-citation Matrix
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> matrix = co_citation_matrix(directory=directory)
>>> matrix.head()
document                                                                            Davis FD et al, 1989, MIS QUART MANAGE INF SYST  ... Goo JJ et al, 2020, J OPEN INNOV: TECHNOL MARK CO
global_citations                                                                                                              25830  ...                                             15   
local_citations                                                                                                                  14  ...                                                6 
document                                           global_citations local_citations                                                  ...                                                  
Davis FD et al, 1989, MIS QUART MANAGE INF SYST    25830            14                                                         14.0  ...                                               0.0
Venkatesh V et al, 2000, MANAGE SCI                9760             7                                                           4.0  ...                                               1.0
Venkatesh V et al, 2003, MIS QUART MANAGE INF SYST 16860            9                                                           5.0  ...                                               1.0
Lee M-C et al, 2009, ELECT COMMER RES APPL         876              9                                                           4.0  ...                                               0.0
Lin M et al, 2013, MANAGE SCI                      553              6                                                           0.0  ...                                               0.0
<BLANKLINE>
[5 rows x 50 columns]


"""
from os.path import join

import numpy as np
import pandas as pd

from .load_references import load_references
from .records2documents import records2documents


def co_citation_matrix(top_n=50, directory="./"):

    # ---< obtains the most local cited references >-------------------------------------
    references = load_references(directory)
    references = references.sort_values("local_citations", ascending=False)
    record_no = references.record_no
    record_no = record_no.head(top_n)

    # ---< obtains the document-reference table >----------------------------------------
    cited_references_table = pd.read_csv(
        join(directory, "processed", "cited_references_table.csv")
    )
    cited_references_table = cited_references_table[
        cited_references_table.cited_id.isin(record_no)
    ]

    # ---< document-reference table >----------------------------------------------------
    cited_references_table["n_citations"] = 1
    ## to check >>>
    cited_references_table = cited_references_table.drop_duplicates()
    ## <<<
    document_reference = cited_references_table.pivot(
        index="citing_id", columns="cited_id", values="n_citations"
    ).fillna(0)

    matrix_values = np.matmul(
        document_reference.transpose().values, document_reference.values
    )

    # ---< index based on citations >----------------------------------------------------
    record_no2global_citations = dict(
        zip(references.record_no, references.global_citations)
    )
    record_no2local_citations = dict(
        zip(references.record_no, references.local_citations)
    )
    global_citations = [
        record_no2global_citations[record_no]
        for record_no in document_reference.columns
    ]
    local_citations = [
        record_no2local_citations[record_no] for record_no in document_reference.columns
    ]
    new_index = pd.MultiIndex.from_tuples(
        [
            (record_no, global_citation, local_citation)
            for record_no, global_citation, local_citation in zip(
                document_reference.columns, global_citations, local_citations
            )
        ],
    )

    # -----------------------------------------------------------------------------------

    co_occ_matrix = pd.DataFrame(
        matrix_values,
        columns=new_index,
        index=new_index,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    co_occ_matrix = co_occ_matrix.loc[:, (co_occ_matrix != 0).any(axis=0)]
    co_occ_matrix = co_occ_matrix.loc[(co_occ_matrix != 0).any(axis=1), :]

    # ---< author, year refereces >------------------------------------------------------
    documents = pd.read_csv(join(directory, "processed", "references.csv"))
    co_occ_matrix = records2documents(matrix=co_occ_matrix, documents=documents)

    return co_occ_matrix
