# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cross-correlation Matrix
===============================================================================

>>> from techminer2.correlation_analysis import cross_correlation_matrix
>>> matrix = cross_correlation_matrix(
...     #
...     # FUNCTION PARAMS:
...     rows_and_columns='authors', 
...     cross_with='countries',
...     method="pearson",
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_.round(3)
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

>>> matrix.list_cells_.head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185      1.000000
1  Arner DW 3:185   Buckley RP 3:185      1.000000
2  Arner DW 3:185  Barberis JN 2:161      0.907242
3  Arner DW 3:185     Butler T 2:041      0.000000
4  Arner DW 3:185     Hamdan A 2:018      0.000000


>>> print(matrix.prompt_)
Analyze the table below which contains the cross-correlation values for the \\
authors based on the values of the countries. High correlation values \\
indicate that the topics in authors are related based on the values of the \\
countries. Identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
|                   |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Butler T 2:041 |   Hamdan A 2:018 |   Turki M 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |
|:------------------|-----------------:|-------------------:|--------------------:|-----------------:|-----------------:|----------------:|--------------:|----------------:|------------------:|----------------:|
| Arner DW 3:185    |            1     |              1     |               0.907 |            0     |                0 |               0 |         0     |           0     |             0     |           0     |
| Buckley RP 3:185  |            1     |              1     |               0.907 |            0     |                0 |               0 |         0     |           0     |             0     |           0     |
| Barberis JN 2:161 |            0.907 |              0.907 |               1     |            0     |                0 |               0 |         0     |           0     |             0     |           0     |
| Butler T 2:041    |            0     |              0     |               0     |            1     |                0 |               0 |         0.283 |           0.283 |             0.886 |           0.886 |
| Hamdan A 2:018    |            0     |              0     |               0     |            0     |                1 |               1 |         0     |           0     |             0     |           0     |
| Turki M 2:018     |            0     |              0     |               0     |            0     |                1 |               1 |         0     |           0     |             0     |           0     |
| Lin W 2:017       |            0     |              0     |               0     |            0.283 |                0 |               0 |         1     |           1     |             0     |           0     |
| Singh C 2:017     |            0     |              0     |               0     |            0.283 |                0 |               0 |         1     |           1     |             0     |           0     |
| Brennan R 2:014   |            0     |              0     |               0     |            0.886 |                0 |               0 |         0     |           0     |             1     |           1     |
| Crane M 2:014     |            0     |              0     |               0     |            0.886 |                0 |               0 |         0     |           0     |             1     |           1     |
```
<BLANKLINE>

    

"""
from dataclasses import dataclass

from ..co_occurrence_analysis.co_occurrence_matrix import co_occurrence_matrix
from ..format_prompt_for_dataframes import format_prompt_for_dataframes
from .compute_corr_matrix import compute_corr_matrix


def cross_correlation_matrix(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    cross_with,
    method="pearson",
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Compute the cross-correlation matrix.

    :meta private:
    """
    #
    # Main:
    #
    data_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=rows_and_columns,
        rows=cross_with,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    corr_matrix = compute_corr_matrix(method, data_matrix)

    prompt = __prompt(corr_matrix, rows_and_columns, cross_with)

    @dataclass
    class Results:
        df_ = corr_matrix
        prompt_ = prompt

        @property
        def list_cells_(self):
            matrix = self.df_.copy()
            matrix = matrix.melt(
                value_name="matrix_value",
                var_name="row",
                ignore_index=False,
            )
            matrix["column"] = matrix.index.to_list()
            matrix = matrix.reset_index(drop=True)
            matrix = matrix[["row", "column", "matrix_value"]]

            return matrix

        @property
        def heat_map_(self):
            #
            def make_heat_map(styler):
                styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="Oranges")
                return styler

            return self.df_.style.pipe(make_heat_map)

    return Results()


def __prompt(corr_matrix, rows_and_columns, cross_with):
    """Creates a co-occurrence matrix prompt."""

    corr_matrix = corr_matrix.copy()
    corr_matrix[corr_matrix < 0] = 0

    main_text = (
        "Analyze the table below which contains the cross-correlation "
        f"values for the {rows_and_columns} based on the values "
        f"of the {cross_with}. High correlation values "
        f"indicate that the topics in {rows_and_columns} are "
        f"related based on the values of the {cross_with}. "
        "Identify any notable patterns, trends, or outliers in the data, "
        "and discuss their implications for the research field. Be sure "
        "to provide a concise summary of your findings in no more than "
        "150 words."
    )

    return format_prompt_for_dataframes(main_text, corr_matrix.round(3).to_markdown())
