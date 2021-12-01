"""
Coupling by column matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coupling_by_column_matrix(
...     column='author_keywords',
...     min_occ=6, 
...     top_n=15,
...     directory=directory,
... ).head()
           2016-0000  2016-0001  2017-0000  ...  2018-0003  2018-0006  2019-0000
2016-0000          4          1          0  ...          1          0          0
2016-0001          1          2          1  ...          1          1          1
2017-0000          0          1          2  ...          1          1          1
2017-0001          0          1          2  ...          1          1          1
2018-0001          1          1          1  ...          3          1          1
<BLANKLINE>
[5 rows x 9 columns]



"""
import numpy as np
import pandas as pd

from .tf_matrix import tf_matrix
from .utils import *
from .utils import index_terms2counters, load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def coupling_by_column_matrix(
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
