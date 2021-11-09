"""
TF-IDF Matrix
===============================================================================

"""
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer


def tfidf_matrix(
    tfmatrix,
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

    result = (
        TfidfTransformer(
            norm=norm, use_idf=use_idf, smooth_idf=smooth_idf, sublinear_tf=sublinear_tf
        )
        .fit_transform(tfmatrix)
        .toarray()
    )

    result = pd.DataFrame(result, columns=tfmatrix.columns, index=tfmatrix.index)

    return result
