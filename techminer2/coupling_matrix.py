"""
Coupling Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> coupling_matrix(
...     top_n=15,
...     column='references',
...     directory=directory,
... ).head()
document                                                                            Chen T et al, 2016, PROC ACM SIGKDD INT CONF KNOW  ... Saberi S et al, 2019, INT J PROD RES
global_citations                                                                                                                 8178  ...                                 592 
local_citations                                                                                                                     1  ...                                    0
document                                           global_citations local_citations                                                    ...                                     
Chen T et al, 2016, PROC ACM SIGKDD INT CONF KNOW  8178             1                                                              13  ...                                    0
Silver D et al, 2016, NATURE                       6359             1                                                               0  ...                                    0
Lundberg SM et al, 2017, ADV NEURAL INF PROCES ... 1949             2                                                               0  ...                                    0
Geissdoerfer M et al, 2017, J CLEAN PROD           1600             0                                                               0  ...                                    0
Young T et al, 2018, IEEE COMPUT INTELL MAG        1071             1                                                               0  ...                                    0
<BLANKLINE>
[5 rows x 15 columns]

>>> coupling_matrix(
...     column='author_keywords',
...     min_occ=3, 
...     top_n=50,
...     directory=directory,
... ).head()
document                                                                   Schueffel P et al, 2016, J INNOV MANAG  ... Kou G et al, 2021, FINANCIAL INNOV
global_citations                                                                                              106  ...                                14 
local_citations                                                                                                14  ...                                 0 
document                                  global_citations local_citations                                         ...                                   
Schueffel P et al, 2016, J INNOV MANAG    106              14                                                   5  ...                                  0
Zavolokina L et al, 2016, FINANCIAL INNOV 43               7                                                    1  ...                                  0
Hung J-L et al, 2016, FINANCIAL INNOV     24               4                                                    0  ...                                  0
Kotarba M et al, 2016, FOUND MANAG        16               3                                                    1  ...                                  0
Gabor D et al, 2017, NEW POLIT ECON       146              15                                                   0  ...                                  0
<BLANKLINE>
[5 rows x 39 columns]


"""
from os.path import join

import numpy as np
import pandas as pd

from ._read_records import read_all_records, read_filtered_records
from .records2documents import records2documents
from .tf_matrix import tf_matrix

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def coupling_matrix(
    column,
    top_n=100,
    min_occ=1,
    metric="global_citations",
    directory="./",
):
    if column == "references":
        matrix = coupling_by_references_matrix_(
            top_n=top_n,
            metric=metric,
            directory=directory,
        )
        documents = pd.read_csv(join(directory, "processed", "references.csv"))

    else:
        matrix = coupling_by_column_matrix_(
            column=column,
            min_occ=min_occ,
            top_n=top_n,
            metric=metric,
            directory=directory,
        )
        documents = read_all_records(directory=directory)

    matrix = records2documents(matrix=matrix, documents=documents)
    return matrix


# ---------------------------------------------------------------------------------------


def coupling_by_references_matrix_(
    top_n=100,
    metric="global_citations",
    directory="./",
):
    # selects the top_n most cited documents
    documents = load_filtered_documents(directory=directory)
    documents = documents.sort_values(by=metric, ascending=False)
    documents = documents.head(top_n)
    record_no = documents.record_no.values.copy()

    # loads the cited references table
    cited_references = pd.read_csv(
        join(directory, "processed", "cited_references_table.csv")
    )
    cited_references = cited_references.loc[
        cited_references.citing_id.map(lambda x: x in record_no)
    ]
    cited_references["value"] = 1

    cited_references = cited_references.drop_duplicates()

    matrix_in_columns = cited_references.pivot(
        index="citing_id", columns="cited_id", values="value"
    )

    matrix_in_columns = matrix_in_columns.fillna(0)

    matrix_values = np.matmul(
        matrix_in_columns.values, matrix_in_columns.transpose().values
    )

    # ---< index based on citations >----------------------------------------------------
    record_no2global_citations = dict(
        zip(documents.record_no, documents.global_citations)
    )
    record_no2local_citations = dict(
        zip(documents.record_no, documents.local_citations)
    )
    global_citations = [
        record_no2global_citations[record_no] for record_no in matrix_in_columns.index
    ]
    local_citations = [
        record_no2local_citations[record_no] for record_no in matrix_in_columns.index
    ]
    new_index = pd.MultiIndex.from_tuples(
        [
            (record_no, global_citation, local_citation)
            for record_no, global_citation, local_citation in zip(
                matrix_in_columns.index, global_citations, local_citations
            )
        ],
    )

    # -----------------------------------------------------------------------------------

    coupling_matrix = pd.DataFrame(
        matrix_values,
        columns=new_index,
        index=new_index,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    coupling_matrix = coupling_matrix.loc[:, (coupling_matrix != 0).any(axis=0)]
    coupling_matrix = coupling_matrix.loc[(coupling_matrix != 0).any(axis=1), :]

    coupling_matrix = coupling_matrix.astype(int)

    return coupling_matrix


# ---------------------------------------------------------------------------------------


def coupling_by_column_matrix_(
    column,
    min_occ=1,
    top_n=100,
    metric="global_citations",
    sep="; ",
    directory="./",
):

    matrix_in_columns = tf_matrix(
        directory=directory,
        column=column,
        min_occ=min_occ,
        sep=sep,
    )

    documents = load_filtered_documents(directory=directory)
    documents = documents.sort_values(by=metric, ascending=False)
    record_no = documents.head(top_n).record_no.values.copy()

    matrix_in_columns = matrix_in_columns.loc[
        matrix_in_columns.index.intersection(record_no)
    ]

    matrix_values = np.matmul(
        matrix_in_columns.values, matrix_in_columns.transpose().values
    )

    # ---< index based on citations >----------------------------------------------------
    record_no2global_citations = dict(
        zip(documents.record_no, documents.global_citations)
    )
    record_no2local_citations = dict(
        zip(documents.record_no, documents.local_citations)
    )
    global_citations = [
        record_no2global_citations[record_no] for record_no in matrix_in_columns.index
    ]
    local_citations = [
        record_no2local_citations[record_no] for record_no in matrix_in_columns.index
    ]
    new_index = pd.MultiIndex.from_tuples(
        [
            (record_no, global_citation, local_citation)
            for record_no, global_citation, local_citation in zip(
                matrix_in_columns.index, global_citations, local_citations
            )
        ],
    )

    # -----------------------------------------------------------------------------------

    coupling_matrix = pd.DataFrame(
        matrix_values,
        columns=new_index,
        index=new_index,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    coupling_matrix = coupling_matrix.loc[:, (coupling_matrix != 0).any(axis=0)]
    coupling_matrix = coupling_matrix.loc[(coupling_matrix != 0).any(axis=1), :]

    coupling_matrix = coupling_matrix.astype(int)

    return coupling_matrix
