"""
Cross-correlation Matrix List (GPT)
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import vantagepoint
>>> directory = "data/regtech/"

>>> r = vantagepoint.analyze.matrix.cross_corr_matrix_list(
...     criterion_for_columns='authors',
...     criterion_for_rows="author_keywords",
...     topics_length=10,
...     directory=directory,
... )
>>> r.matrix_.head()
                 row             column  CORR
0     Arner DW 3:185     Arner DW 3:185   1.0
1  Barberis JN 2:161  Barberis JN 2:161   1.0
2    Brennan R 2:014    Brennan R 2:014   1.0
3    Brennan R 2:014      Crane M 2:014   1.0
4   Buckley RP 3:185   Buckley RP 3:185   1.0


>>> print(r.prompt_)
Analyze the table below which contains the cross-correlation values for the authors based on the values of the author_keywords. High correlation values indicate that the topics in authors are related based on the values of the author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row               | column            |   CORR |
|---:|:------------------|:------------------|-------:|
|  3 | Brennan R 2:014   | Crane M 2:014     |  1     |
|  9 | Hamdan A 2:018    | Turki M 2:018     |  1     |
| 11 | Lin W 2:017       | Singh C 2:017     |  1     |
| 16 | Arner DW 3:185    | Buckley RP 3:185  |  1     |
| 18 | Arner DW 3:185    | Barberis JN 2:161 |  0.873 |
| 20 | Barberis JN 2:161 | Buckley RP 3:185  |  0.873 |
| 22 | Brennan R 2:014   | Lin W 2:017       |  0.452 |
| 23 | Brennan R 2:014   | Singh C 2:017     |  0.452 |
| 24 | Crane M 2:014     | Lin W 2:017       |  0.452 |
| 25 | Crane M 2:014     | Singh C 2:017     |  0.452 |
| 30 | Arner DW 3:185    | Butler T/1 2:041  |  0.375 |
| 31 | Buckley RP 3:185  | Butler T/1 2:041  |  0.375 |
| 34 | Arner DW 3:185    | Lin W 2:017       |  0.302 |
| 35 | Arner DW 3:185    | Singh C 2:017     |  0.302 |
| 36 | Buckley RP 3:185  | Lin W 2:017       |  0.302 |
| 37 | Buckley RP 3:185  | Singh C 2:017     |  0.302 |
| 42 | Butler T/1 2:041  | Lin W 2:017       |  0.302 |
| 43 | Butler T/1 2:041  | Singh C 2:017     |  0.302 |
| 46 | Barberis JN 2:161 | Lin W 2:017       |  0.263 |
| 47 | Barberis JN 2:161 | Singh C 2:017     |  0.263 |
| 50 | Arner DW 3:185    | Brennan R 2:014   |  0.25  |
| 51 | Arner DW 3:185    | Crane M 2:014     |  0.25  |
| 53 | Brennan R 2:014   | Buckley RP 3:185  |  0.25  |
| 54 | Brennan R 2:014   | Butler T/1 2:041  |  0.25  |
| 56 | Buckley RP 3:185  | Crane M 2:014     |  0.25  |
| 58 | Butler T/1 2:041  | Crane M 2:014     |  0.25  |
| 62 | Barberis JN 2:161 | Brennan R 2:014   |  0.218 |
| 63 | Barberis JN 2:161 | Crane M 2:014     |  0.218 |
| 66 | Barberis JN 2:161 | Butler T/1 2:041  |  0.055 |
| 68 | Hamdan A 2:018    | Lin W 2:017       | -0.047 |
| 69 | Hamdan A 2:018    | Singh C 2:017     | -0.047 |
| 71 | Lin W 2:017       | Turki M 2:018     | -0.047 |
| 73 | Singh C 2:017     | Turki M 2:018     | -0.047 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

from ... import chatgpt
from .cross_corr_matrix import cross_corr_matrix
from .list_cells_in_matrix import list_cells_in_matrix


@dataclass(init=False)
class _MatrixResult:
    matrix_: None
    prompt_: None
    method_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def cross_corr_matrix_list(
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
    """Returns an auto-correlation matrix list."""

    results = _MatrixResult()
    results.criterion_for_columns_ = criterion_for_columns
    results.criterion_for_rows_ = criterion_for_rows
    results.method_ = method

    obj = cross_corr_matrix(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        method=method,
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
    )
    results.matrix_ = list_cells_in_matrix(obj.matrix_, value_name="CORR")

    results.prompt_ = chatgpt.generate_prompt_for_cross_corr_matrix_list(results)

    return results
