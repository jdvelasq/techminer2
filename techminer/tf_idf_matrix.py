"""
TF-IDF matrix
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> tf_idf_matrix(directory, 'authors', min_occ=6).head()
authors     Rabbani MR  Arner DW Reyes-Mercado P Wojcik D Buckley RP Khan S  \\
#d                  10         9               7        7          7      6    
#c                  69       135               0       49        132     49    
document_id                                                                   
2016-0018          0.0  1.000000             0.0      0.0   0.000000    0.0   
2017-0005          0.0  0.680044             0.0      0.0   0.733171    0.0   
2017-0016          0.0  0.000000             0.0      0.0   0.000000    0.0   
2017-0057          0.0  0.000000             0.0      0.0   0.000000    0.0   
2018-0003          0.0  0.000000             0.0      0.0   0.000000    0.0   
.
authors     Ozili PK Gozman DP Serrano W Wonglimpiyarat J Schwienbacher A  
#d                6          6         6                6               6   
#c               151        26        15               52              50   
document_id                                                                
2016-0018        0.0       0.0       0.0              0.0             0.0  
2017-0005        0.0       0.0       0.0              0.0             0.0  
2017-0016        0.0       0.0       0.0              1.0             0.0  
2017-0057        0.0       0.0       0.0              1.0             0.0  
2018-0003        1.0       0.0       0.0              0.0             0.0
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
