"""
Term-frequency matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> tf_matrix(directory, 'authors', min_occ=6).head()
authors     Rabbani MR Arner DW Reyes-Mercado P Wojcik D Buckley RP Khan S  \\
#d                  10        9               7        7          7      6    
#c                   6      135               0       49        132     49    
document_id                                                                  
2015-0001            0        0               0        0          0      0   
2015-0002            0        0               0        0          0      0   
2015-0003            0        0               0        0          0      0   
2015-0004            0        0               0        0          0      0   
2015-0006            0        0               0        0          0      0   
-
authors     Ozili PK Gozman DP Serrano W Wonglimpiyarat J Schwienbacher A  
#d                 6         6         6                6               6   
#c               151        26        15               52              50   
document_id                                                                
2015-0001          0         0         0                0               0  
2015-0002          0         0         0                0               0  
2015-0003          0         0         0                0               0  
2015-0004          0         0         0                0               0  
2015-0006          0         0         0                0               0


"""
import numpy as np
import pandas as pd

from .utils import *

# pylint: disable=too-many-arguments


def tf_matrix(
    directory,
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    sep="; ",
):

    documents = load_filtered_documents(directory)

    documents = documents[[column, "document_id"]].copy()
    documents["value"] = 1.0
    documents = explode(documents, column, sep)

    grouped_records = documents.groupby([column, "document_id"], as_index=False).agg(
        {"value": np.sum}
    )
    result = pd.pivot_table(
        data=grouped_records,
        index="document_id",
        columns=column,
        margins=False,
        fill_value=0.0,
    )

    result.columns = [b for _, b in result.columns]

    terms = result.sum(axis=0)
    terms = terms.sort_values(ascending=False)
    if min_occ is not None:
        terms = terms[terms >= min_occ]
    if max_occ is not None:
        terms = terms[terms <= max_occ]
    terms = terms.drop(labels=load_stopwords(directory), errors="ignore")
    result = result.loc[:, terms.index]

    result = index_terms2counters(directory, result, "columns", column, sep)

    if scheme is None or scheme == "raw":
        result = result.astype(int)
    elif scheme == "binary":
        result = result.applymap(lambda w: 1 if w > 0 else 0)
    elif scheme == "log":
        result = result.applymap(lambda x: np.log(x) if x > 0 else 0)
    elif scheme == "sqrt":
        result = result.applymap(lambda x: np.sqrt(x) if x > 0 else 0)
    else:
        raise ValueError("scheme must be 'raw', 'binary', 'log' or 'sqrt'")

    return result
