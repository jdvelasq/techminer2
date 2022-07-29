"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__auto_corr_matrix
>>> vantagepoint__auto_corr_matrix(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
authors            Arner DW 7:220  ...  Mayer N 2:002
authors                            ...               
Arner DW 7:220           1.000000  ...            0.0
Buckley RP 6:217         0.882735  ...            0.0
Barberis JN 4:146        0.662994  ...            0.0
Zetzsche DA 4:092        0.662994  ...            0.0
Brennan R 3:008          0.000000  ...            0.0
Ryan P 3:008             0.000000  ...            0.0
Hamdan A 2:011           0.000000  ...            0.0
Singh C 2:007            0.000000  ...            0.0
Sarea A 2:006            0.000000  ...            0.0
Mayer N 2:002            0.000000  ...            1.0
<BLANKLINE>
[10 rows x 10 columns]


"""
import pandas as pd

from .vantagepoint__tf_matrix import vantagepoint__tf_matrix


def vantagepoint__auto_corr_matrix(
    criterion,
    method="pearson",
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Returns an auto-correlation."""

    tf_matrix = vantagepoint__tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    auto_corr_matrix = pd.DataFrame(
        0.0,
        columns=tf_matrix.columns,
        index=tf_matrix.columns,
    )

    for col in tf_matrix.columns:
        for row in tf_matrix.columns:
            if col == row:
                auto_corr_matrix.loc[row, col] = 1.0
            else:
                matrix = tf_matrix[[col, row]].copy()
                matrix = matrix.loc[(matrix != 0).any(axis=1)]
                matrix = matrix.astype(float)
                sumproduct = matrix[row].mul(matrix[col], axis=0).sum()
                if matrix.shape[0] == 0:
                    corr = 0.0
                elif sumproduct == 0.0:
                    corr = 0.0
                elif matrix.shape[0] == 1:
                    corr = 1.0
                elif matrix.shape[0] > 1:
                    corr = tf_matrix[col].corr(other=tf_matrix[row], method=method)
                else:
                    corr = 0.0
                auto_corr_matrix.loc[row, col] = corr
                auto_corr_matrix.loc[col, row] = corr

    return auto_corr_matrix
