"""
Cross-correlation Matrix (GPT)
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.cross_corr_matrix(
...     criterion_for_columns = 'authors', 
...     criterion_for_rows='countries',
...     topics_length=10,
...     directory=directory,
... )
>>> r.matrix_
                   Arner DW 3:185  ...  Turki M 2:018
Arner DW 3:185           1.000000  ...            0.0
Buckley RP 3:185         1.000000  ...            0.0
Barberis JN 2:161        0.922664  ...            0.0
Brennan R 2:014          0.000000  ...            0.0
Butler T/1 2:041         0.000000  ...            0.0
Crane M 2:014            0.000000  ...            0.0
Hamdan A 2:018           0.000000  ...            1.0
Lin W 2:017             -0.365858  ...            0.0
Singh C 2:017           -0.365858  ...            0.0
Turki M 2:018            0.000000  ...            1.0
<BLANKLINE>
[10 rows x 10 columns]

>>> print(r.prompt_)
Analyze the table below which contains the cross-correlation values for the authors based on the values of the countries. High correlation values indicate that the topics in authors are related based on the values of the countries. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|                   |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Brennan R 2:014 |   Butler T/1 2:041 |   Crane M 2:014 |   Hamdan A 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Turki M 2:018 |
|:------------------|-----------------:|-------------------:|--------------------:|------------------:|-------------------:|----------------:|-----------------:|--------------:|----------------:|----------------:|
| Arner DW 3:185    |            1     |              1     |               0.923 |             0     |              0     |           0     |                0 |        -0.366 |          -0.366 |               0 |
| Buckley RP 3:185  |            1     |              1     |               0.923 |             0     |              0     |           0     |                0 |        -0.366 |          -0.366 |               0 |
| Barberis JN 2:161 |            0.923 |              0.923 |               1     |             0     |              0     |           0     |                0 |        -0.183 |          -0.183 |               0 |
| Brennan R 2:014   |            0     |              0     |               0     |             1     |              0.882 |           1     |                0 |         0     |           0     |               0 |
| Butler T/1 2:041  |            0     |              0     |               0     |             0.882 |              1     |           0.882 |                0 |         0.226 |           0.226 |               0 |
| Crane M 2:014     |            0     |              0     |               0     |             1     |              0.882 |           1     |                0 |         0     |           0     |               0 |
| Hamdan A 2:018    |            0     |              0     |               0     |             0     |              0     |           0     |                1 |         0     |           0     |               1 |
| Lin W 2:017       |           -0.366 |             -0.366 |              -0.183 |             0     |              0.226 |           0     |                0 |         1     |           1     |               0 |
| Singh C 2:017     |           -0.366 |             -0.366 |              -0.183 |             0     |              0.226 |           0     |                0 |         1     |           1     |               0 |
| Turki M 2:018     |            0     |              0     |               0     |             0     |              0     |           0     |                1 |         0     |           0     |               1 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

from ... import chatgpt
from .auto_corr_matrix import _compute_corr_matrix
from .occ_matrix import occ_matrix


@dataclass(init=False)
class _MatrixResult:
    matrix_: None
    prompt_: None
    method_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def cross_corr_matrix(
    criterion_for_columns=None,
    criterion_for_rows=None,
    method="pearson",
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Compute the cross-correlation matrix."""

    results = _MatrixResult()
    results.criterion_for_columns_ = criterion_for_columns
    results.criterion_for_rows_ = criterion_for_rows
    results.method_ = method

    data_matrix = occ_matrix(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    ).matrix_

    results.matrix_ = _compute_corr_matrix(method, data_matrix)

    results.prompt_ = chatgpt.generate_prompt_for_cross_corr_matrix(results)

    return results
