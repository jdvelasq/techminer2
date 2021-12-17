"""
Coupling Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> coupling_matrix(
...     top_n=15,
...     column='references',
...     directory=directory,
... ).head()
                 2016-0000 2016-0001 2017-0000  ... 2019-0001 2019-0002 2019-0003
                       106       43        146  ...       75        60        44 
                        14        7         15  ...        14        7         14
2016-0000 106 14        13         0         0  ...         0         0         0
2016-0001 43  7          0         6         0  ...         0         0         0
2017-0000 146 15         0         0        31  ...         0         0         0
2017-0001 101 16         0         0         0  ...         0         0         0
2018-0000 220 32         0         0         0  ...         0         0         0
<BLANKLINE>
[5 rows x 15 columns]

>>> coupling_matrix(
...     column='author_keywords',
...     min_occ=3, 
...     top_n=50,
...     directory=directory,
... ).head()
                 2016-0000 2016-0001 2016-0002  ... 2021-0000 2021-0001 2021-0002
                       106       43        24   ...       17        15        14 
                        14        7         4   ...        1         2         0 
2016-0000 106 14         4         1         0  ...         0         0         0
2016-0001 43  7          1         3         1  ...         1         1         0
2016-0002 24  4          0         1         1  ...         1         1         0
2016-0003 16  3          0         1         1  ...         1         1         0
2017-0000 146 15         0         1         1  ...         1         1         0
<BLANKLINE>
[5 rows x 39 columns]


"""
from os.path import join

import numpy as np
import pandas as pd

from .tf_matrix import tf_matrix
from .utils import *
from .utils import index_terms2counters, load_filtered_documents

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
        return coupling_by_references_matrix_(
            top_n=top_n,
            metric=metric,
            directory=directory,
        )

    return coupling_by_column_matrix_(
        column=column,
        min_occ=min_occ,
        top_n=top_n,
        metric=metric,
        directory=directory,
    )


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
    cited_references = pd.read_csv(join(directory, "cited_references_table.csv"))
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
