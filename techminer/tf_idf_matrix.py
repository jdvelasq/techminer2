"""
TF-IDF matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> tf_idf_matrix(directory, 'authors', min_occ=6).head()
authors   Rabbani MR  Arner DW Buckley RP  ... Zetzsche D Surjandy Schwienbacher A
#d                10        9          7   ...         6        6               6 
#c               72        154        151  ...        67       19              56 
record_no                                  ...                                    
2016-0023        0.0  1.000000   0.000000  ...        0.0      0.0             0.0
2017-0005        0.0  0.000000   0.000000  ...        0.0      0.0             0.0
2017-0008        0.0  0.682875   0.730535  ...        0.0      0.0             0.0
2017-0021        0.0  0.000000   0.000000  ...        0.0      0.0             0.0
2017-0064        0.0  0.000000   0.000000  ...        0.0      0.0             0.0
<BLANKLINE>
[5 rows x 17 columns]


"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from .tf_matrix import tf_matrix


def tf_idf_matrix(
    directory,
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    sep="; ",
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    max_items=3000,
):
    """
    Compute TF-IDF matrix.

    Parameters
    ----------
    """
    tfmatrix = tf_matrix(
        directory=directory,
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        sep=sep,
    )

    values = (
        TfidfTransformer(
            norm=norm, use_idf=use_idf, smooth_idf=smooth_idf, sublinear_tf=sublinear_tf
        )
        .fit_transform(tfmatrix)
        .toarray()
    )

    tfidf = pd.DataFrame(values, columns=tfmatrix.columns, index=tfmatrix.index)

    return tfidf
