"""
TF-IDF Matrix
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__tf_idf_matrix
>>> vantagepoint__tf_idf_matrix(
...     criterion='authors',
...     topic_min_occ=2,
...     directory=directory,
... ).head()
authors                                             Arner DW 7:220  ...  Mayer N 2:002
article                                                             ...               
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...        0.522776  ...            0.0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...        0.522776  ...            0.0
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55             0.439335  ...            0.0
Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7              0.522776  ...            0.0
Barberis JN, 2016, NEW ECON WINDOWS, P69                  0.629705  ...            0.0
<BLANKLINE>
[5 rows x 15 columns]

"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from .vantagepoint.analyze.tfidf.tf_matrix import tf_matrix


def vantagepoint__tf_idf_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    scheme=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    **filters,
):
    """
    Compute TF-IDF matrix.

    Parameters
    ----------
    """
    tfmatrix = tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        scheme=scheme,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    values = (
        TfidfTransformer(
            norm=norm,
            use_idf=use_idf,
            smooth_idf=smooth_idf,
            sublinear_tf=sublinear_tf,
        )
        .fit_transform(tfmatrix)
        .toarray()
    )

    tfidf = pd.DataFrame(values, columns=tfmatrix.columns, index=tfmatrix.index)

    return tfidf
