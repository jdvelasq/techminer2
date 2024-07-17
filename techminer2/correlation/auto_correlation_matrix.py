# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2.tech_mining.correlation import auto_correlation_matrix
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_.round(3)
                      Jagtiani J. 3:0317  ...  Zavolokina L. 2:0181
Jagtiani J. 3:0317                  1.00  ...                   0.0
Gomber P. 2:1065                    0.00  ...                   0.0
Hornuf L. 2:0358                    0.00  ...                   0.0
Gai K. 2:0323                       0.00  ...                   0.0
Qiu M. 2:0323                       0.00  ...                   0.0
Sun X./3 2:0323                     0.00  ...                   0.0
Lemieux C. 2:0253                   0.77  ...                   0.0
Dolata M. 2:0181                    0.00  ...                   1.0
Schwabe G. 2:0181                   0.00  ...                   1.0
Zavolokina L. 2:0181                0.00  ...                   1.0
<BLANKLINE>
[10 rows x 10 columns]

>>> matrix.list_cells_.head()
                  row              column  matrix_value
0  Jagtiani J. 3:0317  Jagtiani J. 3:0317           1.0
1  Jagtiani J. 3:0317    Gomber P. 2:1065           0.0
2  Jagtiani J. 3:0317    Hornuf L. 2:0358           0.0
3  Jagtiani J. 3:0317       Gai K. 2:0323           0.0
4  Jagtiani J. 3:0317       Qiu M. 2:0323           0.0

>>> print(matrix.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
from dataclasses import dataclass

from ..helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes
from ..metrics.tfidf import tfidf
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

    return helper_format_prompt_for_dataframes(main_text, corr_matrix.round(3).to_markdown())
