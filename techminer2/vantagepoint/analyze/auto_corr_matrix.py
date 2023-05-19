"""
Auto-correlation Matrix (GPT)
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.auto_corr_matrix(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
>>> r.matrix_
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


>>> print(r.prompt_)
Analyze the table below which contains the auto-correlation values for the authors. High correlation values indicate that the topics tends to appear together in the same document and forms a group. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words. 
<BLANKLINE>
|                  |   Arner DW 3:185 |   Buckley RP 3:185 |   Butler T/1 2:041 |   Hamdan A 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |   Sarea A 2:012 |   Grassi L 2:002 |
|:-----------------|-----------------:|-------------------:|-------------------:|-----------------:|--------------:|----------------:|------------------:|----------------:|----------------:|-----------------:|
| Arner DW 3:185   |                1 |                  1 |                  0 |            0     |             0 |               0 |                 0 |               0 |           0     |                0 |
| Buckley RP 3:185 |                1 |                  1 |                  0 |            0     |             0 |               0 |                 0 |               0 |           0     |                0 |
| Butler T/1 2:041 |                0 |                  0 |                  1 |            0     |             0 |               0 |                 0 |               0 |           0     |                0 |
| Hamdan A 2:018   |                0 |                  0 |                  0 |            1     |             0 |               0 |                 0 |               0 |           0.417 |                0 |
| Lin W 2:017      |                0 |                  0 |                  0 |            0     |             1 |               1 |                 0 |               0 |           0     |                0 |
| Singh C 2:017    |                0 |                  0 |                  0 |            0     |             1 |               1 |                 0 |               0 |           0     |                0 |
| Brennan R 2:014  |                0 |                  0 |                  0 |            0     |             0 |               0 |                 1 |               1 |           0     |                0 |
| Crane M 2:014    |                0 |                  0 |                  0 |            0     |             0 |               0 |                 1 |               1 |           0     |                0 |
| Sarea A 2:012    |                0 |                  0 |                  0 |            0.417 |             0 |               0 |                 0 |               0 |           1     |                0 |
| Grassi L 2:002   |                0 |                  0 |                  0 |            0     |             0 |               0 |                 0 |               0 |           0     |                1 |
<BLANKLINE>
<BLANKLINE>


"""
from dataclasses import dataclass

import pandas as pd

from ... import chatgpt
from .tf_matrix import tf_matrix


@dataclass(init=False)
class _MatrixResult:
    matrix_: None
    prompt_: None
    method_: None
    criterion_for_columns_: None
    criterion_for_rows_: None
    metric_: None


def auto_corr_matrix(
    criterion,
    method="pearson",
    topics_length=50,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Returns an auto-correlation."""

    results = _MatrixResult()
    results.criterion_for_columns_ = criterion
    results.criterion_for_rows_ = criterion
    results.method_ = method
    results.metric_ = "CORR"

    data_matrix = tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.matrix_ = _compute_corr_matrix(
        method=method,
        data_matrix=data_matrix,
    )
    results.prompt_ = chatgpt.generate_prompt_for_auto_corr_matrix(results)

    return results


def _compute_corr_matrix(
    method,
    data_matrix,
):
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
