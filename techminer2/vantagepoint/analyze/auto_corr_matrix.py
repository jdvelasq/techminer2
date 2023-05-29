# flake8: noqa
"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> corr_matrix = vantagepoint.analyze.auto_corr_matrix(
...     criterion='authors',
...     topics_length=10,
...     root_dir=root_dir,
... )
>>> corr_matrix.matrix_
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


>>> print(corr_matrix.prompt_)
Analyze the table below which contains the auto-correlation values for the \
authors. High correlation values indicate that the topics tends to appear \
together in the same document and forms a group. Identify any notable \
patterns, trends, or outliers in the data, and discuss their implications \
for the research field. Be sure to provide a concise summary of your \
findings in no more than 150 words.
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

# pylint: disable=line-too-long
"""

from ...classes import CorrMatrix
from .compute_corr_matrix import compute_corr_matrix
from .tf_matrix import tf_matrix


def auto_corr_matrix(
    criterion,
    method="pearson",
    topics_length=50,
    topic_occ_min=None,
    topic_occ_max=None,
    topic_citations_min=None,
    topic_citations_max=None,
    custom_topics=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Returns an auto-correlation."""

    def generate_prompt(obj):
        prompt = (
            "Analyze the table below which contains the auto-correlation "
            f"values for the {obj.criterion_}. High correlation values "
            "indicate that the topics tends to appear together in the same "
            "document and forms a group. Identify any notable patterns, "
            "trends, or outliers in the data, and discuss their implications "
            "for the research field. Be sure to provide a concise summary of "
            "your findings in no more than 150 words."
            f"\n\n{obj.matrix_.round(3).to_markdown()}\n\n"
        )
        return prompt

    #
    # Main:
    #
    data_matrix = tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_occ_min,
        topic_max_occ=topic_occ_max,
        topic_min_citations=topic_citations_min,
        topic_max_citations=topic_citations_max,
        custom_topics=custom_topics,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    corr_matrix = CorrMatrix()
    corr_matrix.criterion_ = criterion
    corr_matrix.other_criterion_ = criterion
    corr_matrix.method_ = method
    corr_matrix.metric_ = "CORR"
    corr_matrix.matrix_ = compute_corr_matrix(
        method=method, data_matrix=data_matrix
    )
    corr_matrix.prompt_ = generate_prompt(corr_matrix)

    return corr_matrix
