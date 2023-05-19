"""
Auto-correlation Matrix List (GPT)
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.auto_corr_matrix_list(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
>>> r.matrix_.head()
                row            column  CORR
0    Arner DW 3:185    Arner DW 3:185   1.0
1    Arner DW 3:185  Buckley RP 3:185   1.0
2   Brennan R 2:014   Brennan R 2:014   1.0
3  Buckley RP 3:185    Arner DW 3:185   1.0
4  Buckley RP 3:185  Buckley RP 3:185   1.0

>>> print(r.prompt_)
Analyze the table below which contains the auto-correlation values for the authors. High correlation values indicate that the topics tends to appear together in the same document and forms a group. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words. 
<BLANKLINE>
|    | row             | column           |   CORR |
|---:|:----------------|:-----------------|-------:|
|  1 | Arner DW 3:185  | Buckley RP 3:185 |  1     |
| 10 | Lin W 2:017     | Singh C 2:017    |  1     |
| 14 | Brennan R 2:014 | Crane M 2:014    |  1     |
| 16 | Hamdan A 2:018  | Sarea A 2:012    |  0.417 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

from ... import chatgpt
from .auto_corr_matrix import auto_corr_matrix
from .matrix_to_matrix_list import matrix_to_matrix_list


@dataclass(init=False)
class _MatrixResult:
    matrix_: None
    prompt_: None
    method_: None
    criterion_: None


def auto_corr_matrix_list(
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
    """Returns an auto-correlation matrix list."""

    results = _MatrixResult()
    results.criterion_ = criterion
    results.method_ = method
    results.matrix_ = _compute_matrix(
        criterion=criterion,
        method=method,
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

    results.prompt_ = chatgpt.generate_prompt_for_auto_corr_matrix_list(results)

    return results


def _compute_matrix(
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
    result = auto_corr_matrix(
        criterion=criterion,
        method=method,
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

    matrix = matrix_to_matrix_list(result.matrix_, value_name="CORR")

    return matrix
