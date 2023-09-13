# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _correlation_analysis.auto_correlation_matrix:

Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2.correlation import auto_correlation_matrix
>>> matrix = auto_correlation_matrix(
...     #
...     # FUNCTION PARAMS:
...     rows_and_columns='authors',
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
Arner DW 3:185               1.00  ...            0.0
Buckley RP 3:185             1.00  ...            0.0
Barberis JN 2:161            0.77  ...            0.0
Butler T 2:041               0.00  ...            0.0
Hamdan A 2:018               0.00  ...            0.0
Turki M 2:018                0.00  ...            0.0
Lin W 2:017                  0.00  ...            0.0
Singh C 2:017                0.00  ...            0.0
Brennan R 2:014              0.00  ...            1.0
Crane M 2:014                0.00  ...            1.0
<BLANKLINE>
[10 rows x 10 columns]

>>> matrix.list_cells_.head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185        1.0000
1  Arner DW 3:185   Buckley RP 3:185        1.0000
2  Arner DW 3:185  Barberis JN 2:161        0.7698
3  Arner DW 3:185     Butler T 2:041        0.0000
4  Arner DW 3:185     Hamdan A 2:018        0.0000

>>> print(matrix.prompt_)
Your task is to generate a short paragraph of a research paper analyzing \\
the auto-correlation values between the items of the column 'authors' of \\
a bibliographic dataset.  Analyze the table below which contains the \\
auto-correlation values for the 'authors'. High correlation values \\
indicate that the items tends to appear together in the same document and \\
forms a group. Identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings, in at most 50 words.
<BLANKLINE>
Table:
```
|                   |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Butler T 2:041 |   Hamdan A 2:018 |   Turki M 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |
|:------------------|-----------------:|-------------------:|--------------------:|-----------------:|-----------------:|----------------:|--------------:|----------------:|------------------:|----------------:|
| Arner DW 3:185    |             1    |               1    |                0.77 |                0 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Buckley RP 3:185  |             1    |               1    |                0.77 |                0 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Barberis JN 2:161 |             0.77 |               0.77 |                1    |                0 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Butler T 2:041    |             0    |               0    |                0    |                1 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Hamdan A 2:018    |             0    |               0    |                0    |                0 |                1 |               1 |             0 |               0 |                 0 |               0 |
| Turki M 2:018     |             0    |               0    |                0    |                0 |                1 |               1 |             0 |               0 |                 0 |               0 |
| Lin W 2:017       |             0    |               0    |                0    |                0 |                0 |               0 |             1 |               1 |                 0 |               0 |
| Singh C 2:017     |             0    |               0    |                0    |                0 |                0 |               0 |             1 |               1 |                 0 |               0 |
| Brennan R 2:014   |             0    |               0    |                0    |                0 |                0 |               0 |             0 |               0 |                 1 |               1 |
| Crane M 2:014     |             0    |               0    |                0    |                0 |                0 |               0 |             0 |               0 |                 1 |               1 |
```
<BLANKLINE>


"""
from dataclasses import dataclass

from ..format_prompt_for_dataframes import format_prompt_for_dataframes
from ..performance.tfidf import tfidf
from .compute_corr_matrix import compute_corr_matrix


def auto_correlation_matrix(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
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
    """Returns an auto-correlation.

    :meta private:
    """

    data_matrix = tfidf(
        #
        # TF PARAMS:
        field=rows_and_columns,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    custom_items = [" ".join(col.split(" ")[:-1]) for col in data_matrix.columns.tolist()]

    corr_matrix = compute_corr_matrix(method=method, data_matrix=data_matrix)

    prompt = __prompt(corr_matrix, rows_and_columns)

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


def __prompt(corr_matrix, rows_and_columns):
    """Creates a co-occurrence matrix prompt."""

    corr_matrix = corr_matrix.copy()
    corr_matrix[corr_matrix < 0] = 0

    main_text = (
        "Your task is to generate a short paragraph of a research paper "
        "analyzing the auto-correlation values between the items of the "
        f"column '{rows_and_columns}' of a bibliographic dataset.\n\n"
        "Analyze the table below which contains the auto-correlation "
        f"values for the '{rows_and_columns}'. High correlation values "
        "indicate that the items tends to appear together in the same "
        "document and forms a group. Identify any notable patterns, "
        "trends, or outliers in the data, and discuss their implications "
        "for the research field. Be sure to provide a concise summary of "
        "your findings, in at most 50 words."
    )

    return format_prompt_for_dataframes(main_text, corr_matrix.round(3).to_markdown())
