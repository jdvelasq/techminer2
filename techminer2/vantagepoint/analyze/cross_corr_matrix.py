# flake8: noqa
"""
Cross-correlation Matrix
===============================================================================



>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> corr_matrix = vantagepoint.analyze.cross_corr_matrix(
...     criterion = 'authors', 
...     other_criterion='countries',
...     topics_length=10,
...     root_dir=root_dir,
... )
>>> corr_matrix.matrix_
                   Arner DW 3:185  ...  Crane M 2:014
Arner DW 3:185           1.000000  ...       0.000000
Buckley RP 3:185         1.000000  ...       0.000000
Barberis JN 2:161        0.922664  ...       0.000000
Butler T/1 2:041         0.000000  ...       0.882498
Hamdan A 2:018           0.000000  ...       0.000000
Turki M 2:018            0.000000  ...       0.000000
Lin W 2:017             -0.365858  ...       0.000000
Singh C 2:017           -0.365858  ...       0.000000
Brennan R 2:014          0.000000  ...       1.000000
Crane M 2:014            0.000000  ...       1.000000
<BLANKLINE>
[10 rows x 10 columns]

>>> print(corr_matrix.prompt_)
Analyze the table below which contains the cross-correlation values for the \
authors based on the values of the countries. High correlation values \
indicate that the topics in authors are related based on the values of the \
countries. Identify any notable patterns, trends, or outliers in the data, \
and discuss their implications for the research field. Be sure to provide a \
concise summary of your findings in no more than 150 words.
<BLANKLINE>
|                   |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Butler T/1 2:041 |   Hamdan A 2:018 |   Turki M 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |
|:------------------|-----------------:|-------------------:|--------------------:|-------------------:|-----------------:|----------------:|--------------:|----------------:|------------------:|----------------:|
| Arner DW 3:185    |            1     |              1     |               0.923 |              0     |                0 |               0 |        -0.366 |          -0.366 |             0     |           0     |
| Buckley RP 3:185  |            1     |              1     |               0.923 |              0     |                0 |               0 |        -0.366 |          -0.366 |             0     |           0     |
| Barberis JN 2:161 |            0.923 |              0.923 |               1     |              0     |                0 |               0 |        -0.183 |          -0.183 |             0     |           0     |
| Butler T/1 2:041  |            0     |              0     |               0     |              1     |                0 |               0 |         0.226 |           0.226 |             0.882 |           0.882 |
| Hamdan A 2:018    |            0     |              0     |               0     |              0     |                1 |               1 |         0     |           0     |             0     |           0     |
| Turki M 2:018     |            0     |              0     |               0     |              0     |                1 |               1 |         0     |           0     |             0     |           0     |
| Lin W 2:017       |           -0.366 |             -0.366 |              -0.183 |              0.226 |                0 |               0 |         1     |           1     |             0     |           0     |
| Singh C 2:017     |           -0.366 |             -0.366 |              -0.183 |              0.226 |                0 |               0 |         1     |           1     |             0     |           0     |
| Brennan R 2:014   |            0     |              0     |               0     |              0.882 |                0 |               0 |         0     |           0     |             1     |           1     |
| Crane M 2:014     |            0     |              0     |               0     |              0.882 |                0 |               0 |         0     |           0     |             1     |           1     |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""

from ...classes import CorrMatrix
from .co_occ_matrix import co_occ_matrix
from .compute_corr_matrix import compute_corr_matrix


def cross_corr_matrix(
    criterion,
    other_criterion,
    method="pearson",
    topics_length=None,
    topic_occ_min=None,
    topic_occ_max=None,
    topic_citations_min=None,
    topic_citations_max=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Compute the cross-correlation matrix."""

    def generate_prompt(obj):
        prompt = (
            "Analyze the table below which contains the cross-correlation "
            f"values for the {obj.criterion_} based on the values "
            f"of the {obj.other_criterion_}. High correlation values "
            f"indicate that the topics in {obj.criterion_} are "
            f"related based on the values of the {obj.other_criterion_}. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
            f"\n\n{obj.matrix_.round(3).to_markdown()}\n\n"
        )
        return prompt

    #
    # Main:
    #
    data_matrix = co_occ_matrix(
        columns=criterion,
        rows=other_criterion,
        col_top_n=topics_length,
        col_occ_range=topic_occ_min,
        topic_occ_max=topic_occ_max,
        col_gc_range=topic_citations_min,
        topic_citations_max=topic_citations_max,
        root_dir=root_dir,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    results = CorrMatrix()
    results.criterion_ = criterion
    results.other_criterion_ = other_criterion
    results.method_ = method
    results.metric_ = "CORR"
    results.matrix_ = compute_corr_matrix(method, data_matrix)
    results.prompt_ = generate_prompt(results)

    return results
