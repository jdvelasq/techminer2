"""
TF Matrix
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> tf_matrix('authors', min_occ=2, directory=directory).head()
authors   Wojcik D Rabbani MR Hornuf L  ... Giudici P Iman N Zavolokina L
#d               5          3        3  ...         2      2            2
#c             19         39       110  ...       18     19           54 
record_no                               ...                              
2016-0001        0          0        0  ...         0      0            1
2017-0006        0          0        0  ...         0      0            1
2017-0008        0          0        0  ...         0      0            0
2018-0000        0          0        0  ...         0      0            0
2018-0004        0          0        0  ...         0      0            0
<BLANKLINE>
[5 rows x 38 columns]

"""
import numpy as np
import pandas as pd

from .index_terms2counters import index_terms2counters
from .load_filtered_documents import load_filtered_documents
from .load_stopwords import load_stopwords

# pylint: disable=too-many-arguments


def tf_matrix(
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    sep="; ",
    directory="./",
):

    documents = load_filtered_documents(directory)

    documents = documents.reset_index()
    documents = documents[[column, "record_no"]].copy()
    documents["value"] = 1
    documents[column] = documents[column].str.split(sep)
    documents = documents.explode(column)
    # documents = explode(documents, column, sep)

    grouped_records = documents.groupby(["record_no", column], as_index=False).agg(
        {"value": np.sum}
    )

    result = pd.pivot(
        index="record_no",
        data=grouped_records,
        columns=column,
    )
    result = result.fillna(0)

    # ----< Counts term occurrence >-------------------------------------------
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

    # ---< Remove rows with only zeros detected -------------------------------
    result = result.loc[(result != 0).any(axis=1)]

    # ----< Applies scheme >---------------------------------------------------
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

    result = result.sort_index(axis=0, ascending=True)

    return result
