# flake8: noqa
"""
TF-IDF Matrix --- ChatGPT
===============================================================================



>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> tf_matrix = techminer2plus.system.analyze.tf_matrix(
...     field='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> tfidf_matrix = techminer2plus.system.analyze.tf_idf_matrix(tf_matrix)
>>> tfidf_matrix.table_.head()
authors                                             Arner DW 3:185  ...  Arman AA 2:000
article                                                             ...                
Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, ...        0.554789  ...             0.0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...        0.554789  ...             0.0
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...        0.000000  ...             0.0
Buckley RP, 2020, J BANK REGUL, V21, P26                  0.707107  ...             0.0
Butler T/1, 2018, J RISK MANG FINANCIAL INST, V...        0.000000  ...             0.0
<BLANKLINE>
[5 rows x 15 columns]


"""
from typing import Literal

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from ...classes import TFIDFMatrix

# from scipy.sparse import csr_matrix


def tf_idf_matrix(
    obj,
    # TF-IDF parameters
    norm: Literal["l1", "l2", None] = "l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
):
    """
    Compute TF-IDF matrix from a TF matrix.


    """

    transformer = TfidfTransformer(
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
    )

    # sparse_matrix = csr_matrix(obj.table_)
    # transformed_matrix = transformer.fit_transform(sparse_matrix)
    transformed_matrix = transformer.fit_transform(obj.table_)

    tf_idf_matrix_ = TFIDFMatrix()
    tf_idf_matrix_.criterion_ = obj.criterion_
    tf_idf_matrix_.prompt_ = obj.prompt_
    tf_idf_matrix_.table_ = pd.DataFrame(
        # transformed_matrix.reshape(sparse_matrix.shape),
        transformed_matrix.toarray(),
        columns=obj.table_.columns,
        index=obj.table_.index,
    )

    return tf_idf_matrix_
