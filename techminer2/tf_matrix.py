"""
TF Matrix
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> tf_matrix(
...     'authors', 
...     min_occ=2, 
...     directory=directory,
... ).head()
                                                    Arner DW 7:220  ...  Lin W 2:007
article                                                             ...             
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...               1  ...            0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               1  ...            0
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55                    1  ...            0
Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7                     1  ...            0
Barberis JN, 2016, NEW ECON WINDOWS, P69                         1  ...            0
<BLANKLINE>
[5 rows x 15 columns]

"""
import numpy as np
import pandas as pd

from ._read_records import read_records
from .items2counters import items2counters
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

    documents = read_records(directory)

    documents = documents.reset_index()
    documents = documents[[column, "article"]].copy()
    documents["value"] = 1
    documents[column] = documents[column].str.split(sep)
    documents = documents.explode(column)
    # documents = explode(documents, column, sep)

    grouped_records = documents.groupby(["article", column], as_index=False).agg(
        {"value": np.sum}
    )

    result = pd.pivot(
        index="article",
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

    items_dict = items2counters(
        column=column,
        directory=directory,
        database="documents",
        use_filter=True,
    )

    # result = index_terms2counters(directory, result, "columns", column, sep)
    result = result.rename(columns=items_dict)

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
