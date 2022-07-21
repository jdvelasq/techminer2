"""
TF-IDF Matrix
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__tf_idf_matrix
>>> vantagepoint__tf_idf_matrix(
...     'authors', 
...     min_occ=2, 
...     directory=directory,
... ).head()
                                                    Arner DW 7:220  ...  Lin W 2:007
article                                                             ...             
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...        0.522776  ...          0.0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...        0.522776  ...          0.0
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55             0.439335  ...          0.0
Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7              0.522776  ...          0.0
Barberis JN, 2016, NEW ECON WINDOWS, P69                  0.629705  ...          0.0
<BLANKLINE>
[5 rows x 15 columns]

"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from .vantagepoint__tf_matrix import vantagepoint__tf_matrix


def vantagepoint__tf_idf_matrix(
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
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
    tfmatrix = vantagepoint__tf_matrix(
        directory=directory,
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
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
