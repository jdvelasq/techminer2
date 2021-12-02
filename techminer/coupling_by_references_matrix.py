"""
Coupling by references matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coupling_matrix = coupling_by_references_matrix(
...     top_n=15,
...     directory=directory,
... )
>>> coupling_matrix.head()
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


>>> coupling_network = co_occurrence_network(coupling_matrix)
>>> network_communities(coupling_network)
cluster           CLUST_0           CLUST_1  ...           CLUST_4           CLUST_5
rn                                           ...                                    
0        2016-0000 106:14  2018-0000 220:32  ...  2019-0001 075:14  2019-0002 060:07
1        2018-0001 076:10  2017-0001 101:16  ...                                    
2        2018-0003 067:06  2018-0004 063:08  ...                                    
3        2018-0005 062:09                    ...                                    
4        2019-0003 044:14                    ...                                    
5        2016-0001 043:07                    ...                                    
<BLANKLINE>
[6 rows x 6 columns]

>>> file_name = "/workspaces/techminer-api/sphinx/images/coupling_references_network.png"
>>> network_plot(coupling_network).savefig(file_name)

.. image:: images/coupling_references_network.png
    :width: 550px
    :align: center





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
