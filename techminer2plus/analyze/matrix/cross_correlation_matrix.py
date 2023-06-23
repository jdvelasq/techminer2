# flake8: noqa
"""
Cross-correlation Matrix
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> cross_corr_matrix = techminer2plus.analyze.matrix.cross_correlation_matrix(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> cross_corr_matrix.matrix_.round(3)
                   Arner DW 3:185  ...  Crane M 2:014
Arner DW 3:185              1.000  ...          0.000
Buckley RP 3:185            1.000  ...          0.000
Barberis JN 2:161           0.907  ...          0.000
Butler T 2:041              0.000  ...          0.886
Hamdan A 2:018              0.000  ...          0.000
Turki M 2:018               0.000  ...          0.000
Lin W 2:017                -0.235  ...          0.000
Singh C 2:017              -0.235  ...          0.000
Brennan R 2:014             0.000  ...          1.000
Crane M 2:014               0.000  ...          1.000
<BLANKLINE>
[10 rows x 10 columns]



>>> print(cross_corr_matrix.prompt_)
Analyze the table below which contains the cross-correlation values for the \\
authors based on the values of the countries. High correlation values \\
indicate that the topics in authors are related based on the values of the \\
countries. Identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Matrix:
```
|                   |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Butler T 2:041 |   Hamdan A 2:018 |   Turki M 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |
|:------------------|-----------------:|-------------------:|--------------------:|-----------------:|-----------------:|----------------:|--------------:|----------------:|------------------:|----------------:|
| Arner DW 3:185    |            1     |              1     |               0.907 |            0     |                0 |               0 |        -0.235 |          -0.235 |             0     |           0     |
| Buckley RP 3:185  |            1     |              1     |               0.907 |            0     |                0 |               0 |        -0.235 |          -0.235 |             0     |           0     |
| Barberis JN 2:161 |            0.907 |              0.907 |               1     |            0     |                0 |               0 |        -0.069 |          -0.069 |             0     |           0     |
| Butler T 2:041    |            0     |              0     |               0     |            1     |                0 |               0 |         0.283 |           0.283 |             0.886 |           0.886 |
| Hamdan A 2:018    |            0     |              0     |               0     |            0     |                1 |               1 |         0     |           0     |             0     |           0     |
| Turki M 2:018     |            0     |              0     |               0     |            0     |                1 |               1 |         0     |           0     |             0     |           0     |
| Lin W 2:017       |           -0.235 |             -0.235 |              -0.069 |            0.283 |                0 |               0 |         1     |           1     |             0     |           0     |
| Singh C 2:017     |           -0.235 |             -0.235 |              -0.069 |            0.283 |                0 |               0 |         1     |           1     |             0     |           0     |
| Brennan R 2:014   |            0     |              0     |               0     |            0.886 |                0 |               0 |         0     |           0     |             1     |           1     |
| Crane M 2:014     |            0     |              0     |               0     |            0.886 |                0 |               0 |         0     |           0     |             1     |           1     |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""

from ...classes import CrossCorrMatrix
from ...prompts import format_prompt_for_matrices
from .co_occurrence_matrix import co_occurrence_matrix
from .compute_corr_matrix import compute_corr_matrix


def cross_correlation_matrix(
    rows_and_columns,
    cross_with,
    method="pearson",
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Compute the cross-correlation matrix."""

    def generate_prompt(obj):
        main_text = (
            "Analyze the table below which contains the cross-correlation "
            f"values for the {obj.rows_and_columns_} based on the values "
            f"of the {obj.cross_with_}. High correlation values "
            f"indicate that the topics in {obj.rows_and_columns_} are "
            f"related based on the values of the {obj.cross_with_}. "
            "Identify any notable patterns, trends, or outliers in the data, "
            "and discuss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
        )
        return format_prompt_for_matrices(
            main_text, obj.matrix_.round(3).to_markdown()
        )

    #
    # Main:
    #
    data_matrix = co_occurrence_matrix(
        columns=rows_and_columns,
        rows=cross_with,
        # Columns item filters:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    results = CrossCorrMatrix()
    results.rows_and_columns_ = rows_and_columns
    results.cross_with_ = cross_with
    results.method_ = method
    results.metric_ = "CORR"
    results.matrix_ = compute_corr_matrix(method, data_matrix)
    results.prompt_ = generate_prompt(results)

    return results
