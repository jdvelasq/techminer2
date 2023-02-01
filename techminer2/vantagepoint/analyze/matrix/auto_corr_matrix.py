"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.auto_corr_matrix(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
                  Arner DW 3:185  ...  Grassi L 2:002
Arner DW 3:185               1.0  ...             0.0
Buckley RP 3:185             1.0  ...             0.0
Butler T/1 2:041             0.0  ...             0.0
Hamdan A 2:018               0.0  ...             0.0
Lin W 2:017                  0.0  ...             0.0
Singh C 2:017                0.0  ...             0.0
Brennan R 2:014              0.0  ...             0.0
Crane M 2:014                0.0  ...             0.0
Sarea A 2:012                0.0  ...             0.0
Grassi L 2:002               0.0  ...             1.0
<BLANKLINE>
[10 rows x 10 columns]


"""
import pandas as pd

from ....vantagepoint__tf_matrix import vantagepoint__tf_matrix


def auto_corr_matrix(
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

    data_matrix = vantagepoint__tf_matrix(
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

    corr_matrix = _compute_corr_matrix(method, data_matrix)

    return corr_matrix


def _compute_corr_matrix(method, data_matrix):

    corr_matrix = pd.DataFrame(
        0.0,
        columns=data_matrix.columns.to_list(),
        index=data_matrix.columns.to_list(),
    )

    for col in data_matrix.columns:
        for row in data_matrix.columns:
            if col == row:
                corr_matrix.loc[row, col] = 1.0
            else:
                matrix = data_matrix[[col, row]].copy()
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
                    corr = data_matrix[col].corr(other=data_matrix[row], method=method)
                else:
                    corr = 0.0
                corr_matrix.loc[row, col] = corr
                corr_matrix.loc[col, row] = corr

    return corr_matrix
