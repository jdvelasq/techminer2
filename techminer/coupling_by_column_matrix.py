"""
Coupling by column matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coupling_matrix = coupling_by_column_matrix(
...     column='author_keywords',
...     min_occ=3, 
...     top_n=50,
...     directory=directory,
... )
>>> coupling_matrix.head()
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

>>> coupling_network = co_occurrence_network(coupling_matrix)
>>> network_communities(coupling_network)
cluster           CLUST_0           CLUST_1  ...           CLUST_3           CLUST_4
rn                                           ...                                    
0        2019-0000 097:22  2018-0001 076:10  ...  2017-0000 146:15  2020-0002 018:01
1        2018-0002 067:08  2018-0003 067:06  ...  2017-0001 101:16                  
2        2018-0006 049:10  2019-0003 044:14  ...  2020-0000 026:11                  
3        2018-0007 037:08  2019-0004 035:06  ...  2019-0006 023:07                  
4        2019-0005 033:00  2019-0009 018:07  ...  2020-0004 012:03                  
5        2017-0003 030:02  2021-0002 014:00  ...  2019-0010 012:05                  
6        2016-0002 024:04  2018-0012 014:07  ...                                    
7        2020-0001 019:01  2018-0013 011:01  ...                                    
8        2021-0000 017:01  2020-0005 010:00  ...                                    
9        2016-0003 016:03                    ...                                    
10       2021-0001 015:02                    ...                                    
11       2020-0003 015:06                    ...                                    
12       2019-0012 012:03                    ...                                    
13       2017-0007 011:01                    ...                                    
14       2017-0006 011:03                    ...                                    
<BLANKLINE>
[15 rows x 5 columns]

>>> file_name = "/workspaces/techminer-api/sphinx/images/coupling_column_network.png"
>>> network_plot(coupling_network).savefig(file_name)

.. image:: images/coupling_column_network.png
    :width: 600px
    :align: center

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

    # coupling_matrix = pd.DataFrame(
    #     matrix_values,
    #     columns=matrix_in_columns.index,
    #     index=matrix_in_columns.index,
    # )

    # ---< remove rows and columns with no associations >---------------------------------
    coupling_matrix = coupling_matrix.loc[:, (coupling_matrix != 0).any(axis=0)]
    coupling_matrix = coupling_matrix.loc[(coupling_matrix != 0).any(axis=1), :]

    coupling_matrix = coupling_matrix.astype(int)

    return coupling_matrix
