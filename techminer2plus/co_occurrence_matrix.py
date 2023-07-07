# flake8: noqa
# pylint: disable=line-too-long
"""
.. _co_occurrence_matrix:

Co-occurrence Matrix 
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> co_occ_matrix = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         rows='authors',
...         col_occ_range=(2, None),
...         row_occ_range=(2, None),
...     )
... )
>>> co_occ_matrix
CoocMatrix(columns='author_keywords', rows='authors', dims=(15, 23))

* Functional interface

>>> co_occ_matrix = tm2p.co_occurrence_matrix(
...     columns='author_keywords',
...     rows='authors',
...     col_occ_range=(2, None),
...     row_occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> print(co_occ_matrix)
CoocMatrix(columns='author_keywords', rows='authors', dims=(15, 23))

* Results

>>> co_occ_matrix.df_
column              REGTECH 28:329  ...  REPORTING 02:001
row                                 ...                  
Arner DW 3:185                   2  ...                 0
Buckley RP 3:185                 2  ...                 0
Barberis JN 2:161                1  ...                 0
Butler T 2:041                   2  ...                 0
Hamdan A 2:018                   0  ...                 0
Turki M 2:018                    0  ...                 0
Lin W 2:017                      2  ...                 0
Singh C 2:017                    2  ...                 0
Brennan R 2:014                  2  ...                 0
Crane M 2:014                    2  ...                 0
Ryan P 2:014                     2  ...                 0
Sarea A 2:012                    0  ...                 0
Grassi L 2:002                   2  ...                 1
Lanfranchi D 2:002               2  ...                 1
Arman AA 2:000                   2  ...                 0
<BLANKLINE>
[15 rows x 23 columns]


>>> print(co_occ_matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the 'authors' \\
and 'author_keywords' fields in a bibliographic dataset. Identify any \\
notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| row                |   REGTECH 28:329 |   FINTECH 12:249 |   REGULATORY_TECHNOLOGY 07:037 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   ANTI_MONEY_LAUNDERING 05:034 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   RISK_MANAGEMENT 03:014 |   INNOVATION 03:012 |   SUPTECH 03:004 |   SEMANTIC_TECHNOLOGIES 02:041 |   DATA_PROTECTION 02:027 |   CHARITYTECH 02:017 |   ENGLISH_LAW 02:017 |   ACCOUNTABILITY 02:014 |   DATA_PROTECTION_OFFICER 02:014 |   GDPR 02:014 |   SANDBOXES 02:012 |   TECHNOLOGY 02:010 |   FINANCE 02:001 |   REPORTING 02:001 |
|:-------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|-------------------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------:|--------------------:|-----------------:|-------------------------------:|-------------------------:|---------------------:|---------------------:|------------------------:|---------------------------------:|--------------:|-------------------:|--------------------:|-----------------:|-------------------:|
| Arner DW 3:185     |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           1 |                             2 |                                0 |                        0 |                   0 |                0 |                              0 |                        1 |                    0 |                    0 |                       0 |                                0 |             0 |                  1 |                   0 |                0 |                  0 |
| Buckley RP 3:185   |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           1 |                             2 |                                0 |                        0 |                   0 |                0 |                              0 |                        1 |                    0 |                    0 |                       0 |                                0 |             0 |                  1 |                   0 |                0 |                  0 |
| Barberis JN 2:161  |                1 |                0 |                              0 |                   0 |                   0 |                              0 |                           1 |                             1 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  1 |                   0 |                0 |                  0 |
| Butler T 2:041     |                2 |                2 |                              0 |                   0 |                   1 |                              0 |                           0 |                             0 |                                0 |                        1 |                   0 |                0 |                              2 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Hamdan A 2:018     |                0 |                0 |                              2 |                   0 |                   0 |                              2 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Turki M 2:018      |                0 |                0 |                              2 |                   0 |                   0 |                              2 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Lin W 2:017        |                2 |                0 |                              0 |                   0 |                   0 |                              1 |                           0 |                             0 |                                1 |                        0 |                   0 |                0 |                              0 |                        0 |                    2 |                    2 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Singh C 2:017      |                2 |                0 |                              0 |                   0 |                   0 |                              1 |                           0 |                             0 |                                1 |                        0 |                   0 |                0 |                              0 |                        0 |                    2 |                    2 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Brennan R 2:014    |                2 |                0 |                              0 |                   2 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       2 |                                2 |             2 |                  0 |                   0 |                0 |                  0 |
| Crane M 2:014      |                2 |                0 |                              0 |                   2 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       2 |                                2 |             2 |                  0 |                   0 |                0 |                  0 |
| Ryan P 2:014       |                2 |                0 |                              0 |                   2 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       2 |                                2 |             2 |                  0 |                   0 |                0 |                  0 |
| Sarea A 2:012      |                0 |                0 |                              1 |                   0 |                   0 |                              1 |                           0 |                             0 |                                1 |                        0 |                   0 |                0 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                0 |                  0 |
| Grassi L 2:002     |                2 |                2 |                              1 |                   1 |                   2 |                              0 |                           0 |                             0 |                                0 |                        1 |                   1 |                1 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                1 |                  1 |
| Lanfranchi D 2:002 |                2 |                2 |                              1 |                   1 |                   2 |                              0 |                           0 |                             0 |                                0 |                        1 |                   1 |                1 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   0 |                1 |                  1 |
| Arman AA 2:000     |                2 |                0 |                              0 |                   0 |                   0 |                              0 |                           0 |                             0 |                                0 |                        0 |                   0 |                1 |                              0 |                        0 |                    0 |                    0 |                       0 |                                0 |             0 |                  0 |                   1 |                0 |                  0 |
```
<BLANKLINE>

>>> co_occ_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )
>>> co_occ_matrix
CoocMatrix(columns='author_keywords', rows='author_keywords', dims=(10,
    10))

>>> co_occ_matrix.df_
column                          REGTECH 28:329  ...  RISK_MANAGEMENT 03:014
row                                             ...                        
REGTECH 28:329                              28  ...                       2
FINTECH 12:249                              12  ...                       2
REGULATORY_TECHNOLOGY 07:037                 2  ...                       2
COMPLIANCE 07:030                            7  ...                       1
REGULATION 05:164                            4  ...                       2
ANTI_MONEY_LAUNDERING 05:034                 1  ...                       0
FINANCIAL_SERVICES 04:168                    3  ...                       0
FINANCIAL_REGULATION 04:035                  2  ...                       0
ARTIFICIAL_INTELLIGENCE 04:023               2  ...                       1
RISK_MANAGEMENT 03:014                       2  ...                       3
<BLANKLINE>
[10 rows x 10 columns]


>>> print(co_occ_matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the items of the same column in a bibliographic \\
dataset. Analyze the table below which contains values of co-occurrence \\
(OCC) for the 'author_keywords' field in a bibliographic dataset. Identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| row                            |   REGTECH 28:329 |   FINTECH 12:249 |   REGULATORY_TECHNOLOGY 07:037 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   ANTI_MONEY_LAUNDERING 05:034 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   RISK_MANAGEMENT 03:014 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|-------------------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------:|
| REGTECH 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                              1 |                           3 |                             2 |                                2 |                        2 |
| FINTECH 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                              0 |                           2 |                             1 |                                1 |                        2 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                              2 |                           0 |                             0 |                                1 |                        2 |
| COMPLIANCE 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                              0 |                           0 |                             0 |                                1 |                        1 |
| REGULATION 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                              0 |                           1 |                             0 |                                0 |                        2 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |                0 |                              2 |                   0 |                   0 |                              5 |                           0 |                             0 |                                1 |                        0 |
| FINANCIAL_SERVICES 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                              0 |                           4 |                             2 |                                0 |                        0 |
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           2 |                             4 |                                0 |                        0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                              1 |                           0 |                             0 |                                4 |                        1 |
| RISK_MANAGEMENT 03:014         |                2 |                2 |                              2 |                   1 |                   2 |                              0 |                           0 |                             0 |                                1 |                        3 |
```
<BLANKLINE>

"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Optional

import pandas as pd

from ._chatbot import format_chatbot_prompt_for_df
from ._counters_lib import add_counters_to_frame_axis
from ._filtering_lib import generate_custom_items
from ._metrics_lib import co_occ_matrix_list
from ._sorting_lib import sort_indicators_by_metric, sort_matrix_axis
from .bubble_chart import bubble_chart
from .butterfly_chart import butterfly_chart
from .factor_decomposition_kernel_pca import factor_decomposition_kernel_pca
from .factor_decomposition_pca import factor_decomposition_pca
from .factor_decomposition_svd import factor_decomposition_svd
from .global_indicators_by_field import global_indicators_by_field
from .heat_map import heat_map
from .item_associations import item_associations
from .list_cells_in_matrix import list_cells_in_matrix
from .matrix_viewer import matrix_viewer
from .mds_2d_map import mds_2d_map
from .network_create import network_create


# pylint: disable=too-many-instance-attributes
@dataclass
class CoocMatrix:
    """Co-cccurrence matrix.

    :meta private:
    """

    #
    # PARAMS:
    columns: str
    rows: Optional[str] = None
    #
    # COLUMN PARAMS:
    col_top_n: Optional[int] = None
    col_occ_range: tuple = (None, None)
    col_gc_range: tuple = (None, None)
    col_custom_items: list = datafield(default_factory=list)
    #
    # ROW PARAMS:
    row_top_n: Optional[int] = None
    row_occ_range: tuple = (None, None)
    row_gc_range: tuple = (None, None)
    row_custom_items: list = datafield(default_factory=list)
    #
    # DATABASE PARAMS:
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)
    #
    # RESULTS:
    df_: pd.DataFrame = pd.DataFrame()
    prompt_: str = ""

    def __repr__(self):
        text = "CoocMatrix("
        text += f"columns='{self.columns}'"
        text += f", rows='{self.rows}'"
        text += f", dims={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text

    def list_cells_in_matrix(self):
        """Lists all cells in the matrix."""
        return list_cells_in_matrix(self)

    def heat_map(self, colormap="Blues"):
        """Creates a heat map."""
        return heat_map(self, colormap=colormap)

    def bubble_chart(self, title=None):
        """Creates a bubble chart."""
        return bubble_chart(self, title=title)

    def factor_decomposition_pca(
        self,
        association_index=None,
        n_components=None,
        whiten=False,
        svd_solver="auto",
        tol=0.0,
        iterated_power="auto",
        n_oversamples=10,
        power_iteration_normalizer="auto",
        random_state=0,
    ):
        """Creates a PCA factor matrix."""
        return factor_decomposition_pca(
            cooc_matrix_or_tfidf=self,
            association_index=association_index,
            n_components=n_components,
            whiten=whiten,
            svd_solver=svd_solver,
            tol=tol,
            iterated_power=iterated_power,
            n_oversamples=n_oversamples,
            power_iteration_normalizer=power_iteration_normalizer,
            random_state=random_state,
        )

    def factor_decomposition_svd(
        self,
        association_index=None,
        #
        # SVD PARAMS:
        n_components=None,
        algorithm="randomized",
        n_iter=5,
        n_oversamples=10,
        power_iteration_normalizer="auto",
        random_state=0,
        tol=0.0,
    ):
        """Creates a SVD factor matrix."""
        return factor_decomposition_svd(
            cooc_matrix_or_tfidf=self,
            association_index=association_index,
            #
            # SVD PARAMS:
            n_components=n_components,
            algorithm=algorithm,
            n_iter=n_iter,
            n_oversamples=n_oversamples,
            power_iteration_normalizer=power_iteration_normalizer,
            random_state=random_state,
            tol=tol,
        )

    def factor_decomposition_kernel_pca(
        self,
        association_index=None,
        #
        # KERNEL PCA PARAMS:
        n_components=None,
        kernel="linear",
        gamma=None,
        degree=3,
        coef0=1,
        kernel_params=None,
        alpha=1.0,
        fit_inverse_transform=False,
        eigen_solver="auto",
        tol=0,
        max_iter=None,
        iterated_power="auto",
        remove_zero_eig=False,
        random_state=0,
    ):
        """Kernal PCA"""
        return factor_decomposition_kernel_pca(
            #
            # FUNCTION PARAMS:
            cooc_matrix_or_tfidf=self,
            association_index=association_index,
            #
            # DECOMPOSITION PARAMS:
            n_components=n_components,
            kernel=kernel,
            gamma=gamma,
            degree=degree,
            coef0=coef0,
            kernel_params=kernel_params,
            alpha=alpha,
            fit_inverse_transform=fit_inverse_transform,
            eigen_solver=eigen_solver,
            tol=tol,
            max_iter=max_iter,
            iterated_power=iterated_power,
            remove_zero_eig=remove_zero_eig,
            random_state=random_state,
        )

    def matrix_viewer(
        self,
        #
        # Figure params:
        n_labels=None,
        nx_k=None,
        nx_iterations=30,
        nx_random_state=0,
        node_size_min=30,
        node_size_max=70,
        textfont_size_min=10,
        textfont_size_max=20,
        xaxes_range=None,
        yaxes_range=None,
        show_axes=False,
    ):
        """Creates a network representation."""
        return matrix_viewer(
            cooc_matrix=self,
            #
            # Figure params:
            n_labels=n_labels,
            nx_k=nx_k,
            nx_iterations=nx_iterations,
            nx_random_state=nx_random_state,
            node_size_min=node_size_min,
            node_size_max=node_size_max,
            textfont_size_min=textfont_size_min,
            textfont_size_max=textfont_size_max,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
            show_axes=show_axes,
        )

    def item_associations(self, item):
        """Item associations table"""

        return item_associations(
            item=item,
            cooc_matrix=self,
        )

    def mds_2d_map(
        self,
        association_index=None,
        #
        # MDS params:
        metric=True,
        n_init=4,
        max_iter=300,
        eps=0.001,
        n_jobs=None,
        random_state=0,
        dissimilarity="euclidean",
        #
        # Plot params:
        node_color="#8da4b4",
        node_size_min=12,
        node_size_max=50,
        textfont_size_min=8,
        textfont_size_max=20,
        xaxes_range=None,
        yaxes_range=None,
    ):
        return mds_2d_map(
            cooc_matrix=self,
            association_index=association_index,
            #
            # MDS params:
            metric=metric,
            n_init=n_init,
            max_iter=max_iter,
            eps=eps,
            n_jobs=n_jobs,
            random_state=random_state,
            dissimilarity=dissimilarity,
            #
            # Plot params:
            node_color=node_color,
            node_size_min=node_size_min,
            node_size_max=node_size_max,
            textfont_size_min=textfont_size_min,
            textfont_size_max=textfont_size_max,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

    def network_create(
        self,
        algorithm_or_estimator,
        normalization_index=None,
    ):
        """Creates a network representation."""
        return network_create(
            cooc_matrix=self,
            algorithm_or_estimator=algorithm_or_estimator,
            normalization_index=normalization_index,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def butterfly_chart(
        self,
        item_a,
        item_b,
    ):
        """Butterfly chart"""
        return butterfly_chart(
            cooc_matrix=self,
            item_a=item_a,
            item_b=item_b,
        )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def co_occurrence_matrix(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a co-occurrence matrix."""

    def filter_terms(
        raw_matrix_list,
        name,
        field,
        # Item filters:
        top_n,
        occ_range,
        gc_range,
        custom_items,
    ):
        if custom_items is None:
            indicators = global_indicators_by_field(
                field=field,
                root_dir=root_dir,
                database=database,
                year_filter=year_filter,
                cited_by_filter=cited_by_filter,
                **filters,
            )

            indicators = sort_indicators_by_metric(indicators, "OCC")

            custom_items = generate_custom_items(
                indicators=indicators,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        # custom_items = filter_custom_items_from_column(
        #     dataframe=raw_matrix_list,
        #     col_name=name,
        #     custom_items=custom_items,
        # )

        raw_matrix_list = raw_matrix_list[
            raw_matrix_list[name].isin(custom_items)
        ]

        return raw_matrix_list

    def pivot(matrix_list):
        matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
        matrix = matrix.fillna(0)
        matrix = matrix.astype(int)
        return matrix

    def generate_prompt_for_occ_matrix(matrix, columns, rows):
        """Generates a ChatGPT prompt for a occurrence matrix."""

        main_text = (
            "Your task is to generate a short paragraph for a research paper analyzing "
            "the co-occurrence between the values of different columns in a bibliographic "
            "dataset. Analyze the table below, and delimited by triple backticks, which "
            f"contains values of co-occurrence (OCC) for the '{columns}' and '{rows}' "
            "fields in a bibliographic dataset. Identify any notable patterns, trends, "
            "or outliers in the data, and discuss their implications for the research "
            "field. Be sure to provide a concise summary of your findings in no more "
            "than 150 words."
        )
        return format_chatbot_prompt_for_df(main_text, matrix.to_markdown())

    def generate_prompt_for_co_occ_matrix(matrix, columns):
        """Generates a ChatGPT prompt for a co_occurrence matrix."""

        main_text = (
            "Your task is to generate a short paragraph for a research paper analyzing the "
            "co-occurrence between the items of the same column in a bibliographic dataset. "
            "Analyze the table below which contains values of co-occurrence (OCC) for the "
            f"'{columns}' field in a bibliographic dataset. Identify any notable patterns, "
            "trends, or outliers in the data, and discuss their implications for the research "
            "field. Be sure to provide a concise summary of your findings in no more than 150 "
            "words."
        )
        return format_chatbot_prompt_for_df(main_text, matrix.to_markdown())

    #
    # MAIN CODE:
    #
    if rows is None:
        rows = columns
        row_top_n = col_top_n
        row_occ_range = col_occ_range
        row_gc_range = col_gc_range
        row_custom_items = col_custom_items

    # Generates a matrix list with all descriptors in the database
    raw_matrix_list = co_occ_matrix_list(
        columns=columns,
        rows=rows,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # Filters the terms in the 'row' column of the matrix list
    raw_filterd_matrix_list = filter_terms(
        raw_matrix_list=raw_matrix_list,
        field=rows,
        name="row",
        #
        # ROW PARAMS:
        top_n=row_top_n,
        occ_range=row_occ_range,
        gc_range=row_gc_range,
        custom_items=row_custom_items,
    )

    # Filters the terms in the 'column' column of the matrix list
    filtered_matrix_list = filter_terms(
        raw_matrix_list=raw_filterd_matrix_list,
        field=columns,
        name="column",
        #
        # ROW PARAMS:
        top_n=col_top_n,
        occ_range=col_occ_range,
        gc_range=col_gc_range,
        custom_items=col_custom_items,
    )

    # Creates a matrix
    matrix = pivot(filtered_matrix_list)

    # sort the rows and columns of the matrix
    matrix = sort_matrix_axis(
        matrix,
        axis=0,
        field=rows,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = sort_matrix_axis(
        matrix,
        axis=1,
        field=columns,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    row_custom_items = matrix.index.tolist()
    col_custom_items = matrix.columns.tolist()

    matrix = add_counters_to_frame_axis(
        dataframe=matrix,
        axis=0,
        field=rows,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = add_counters_to_frame_axis(
        dataframe=matrix,
        axis=1,
        field=columns,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if columns == rows:
        prompt = generate_prompt_for_co_occ_matrix(
            matrix,
            columns=columns,
        )
    else:
        prompt = generate_prompt_for_occ_matrix(
            matrix,
            columns=rows,
            rows=columns,
        )

    return CoocMatrix(
        #
        # PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # RESULTS:
        df_=matrix,
        prompt_=prompt,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
