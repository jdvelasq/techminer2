"""
TF-IDF Matrix --- ChatGPT
===============================================================================



>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> tf_matrix = vantagepoint.analyze.tf_matrix(
...     criterion='authors',
...     topic_min_occ=2,
...     root_dir=root_dir,
... )
>>> tfidf_matrix = vantagepoint.analyze.tf_idf_matrix(tf_matrix)
>>> tfidf_matrix.table_.head()
authors                                             Arner DW 3:185  ...  Arman AA 2:000
article                                                             ...                
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FI, ...        0.554789  ...             0.0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...        0.554789  ...             0.0
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...        0.000000  ...             0.0
Buckley RP, 2020, J BANK REGUL, V21, P26                  0.707107  ...             0.0
Butler T/1, 2018, J RISK MANG FIN INST, V11, P19          0.000000  ...             0.0
<BLANKLINE>
[5 rows x 15 columns]


"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from ...classes import TFIDFMatrix


def tf_idf_matrix(
    obj,
    # TF-IDF parameters
    norm="l2",
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

    transformed_matrix = transformer.fit_transform(obj.table_).toarray()

    tf_idf_matrix_ = TFIDFMatrix()
    tf_idf_matrix_.criterion_ = obj.criterion_
    tf_idf_matrix_.prompt_ = obj.prompt_
    tf_idf_matrix_.table_ = pd.DataFrame(
        transformed_matrix, columns=obj.table_.columns, index=obj.table_.index
    )

    return tf_idf_matrix_
