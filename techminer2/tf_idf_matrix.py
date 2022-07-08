"""
TF-IDF Matrix
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> tf_idf_matrix('authors', min_occ=2, directory=directory).head()
authors   Wojcik D Rabbani MR Hornuf L  ...  Zhang MX Daragmeh A Kauffman RJ
#d               5          3        3  ...         2          2           2
#c             19         39       110  ...       12         3           228
record_no                               ...                                 
2016-0001      0.0        0.0      0.0  ...  0.000000        0.0         0.0
2017-0006      0.0        0.0      0.0  ...  0.000000        0.0         0.0
2017-0008      0.0        0.0      0.0  ...  0.707107        0.0         0.0
2018-0000      0.0        0.0      0.0  ...  0.000000        0.0         0.5
2018-0004      0.0        0.0      0.0  ...  0.000000        0.0         0.0
<BLANKLINE>
[5 rows x 38 columns]

"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from .tf_matrix import tf_matrix


def tf_idf_matrix(
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    sep="; ",
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    directory="./",
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
