"""
Coupling by references matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coupling_by_references_matrix(
...     top_n=15,
...     directory=directory,
... ).head()
citing_id  2016-0000  2016-0001  2017-0000  ...  2019-0001  2019-0002  2019-0003
citing_id                                   ...                                 
2016-0000         13          0          0  ...          0          0          0
2016-0001          0          6          0  ...          0          0          0
2017-0000          0          0         31  ...          0          0          0
2017-0001          0          0          0  ...          0          0          0
2018-0000          0          0          0  ...          0          0          0
<BLANKLINE>
[5 rows x 15 columns]


"""
from os.path import join

import numpy as np
import pandas as pd

from .utils import load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def coupling_by_references_matrix(
    top_n=100,
    metric="global_citations",
    sep="; ",
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

    coupling_matrix = pd.DataFrame(
        matrix_values,
        columns=matrix_in_columns.index,
        index=matrix_in_columns.index,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    coupling_matrix = coupling_matrix.loc[:, (coupling_matrix != 0).any(axis=0)]
    coupling_matrix = coupling_matrix.loc[(coupling_matrix != 0).any(axis=1), :]

    coupling_matrix = coupling_matrix.astype(int)

    return coupling_matrix
