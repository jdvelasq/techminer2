# flake8: noqa
# pylint: disable=line-too-long
"""
.. _cross_correlation_matrix:

Cross-correlation Matrix
===============================================================================

* Preparation

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p



* Object oriented interface

>>> cross_corr_matrix = (
...     tm2p.records(root_dir=root_dir)
...     .cross_correlation_matrix(
...         rows_and_columns='authors', 
...         cross_with='countries',
...         top_n=10,
...     )
... )
>>> cross_corr_matrix
CrossCorrMatrix(rows-and-columns='authors', cross-with='countries',
    method='pearson', shape=(10, 10))

* Functional interface

>>> cross_corr_matrix = tm2p.cross_correlation_matrix(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> cross_corr_matrix
CrossCorrMatrix(rows-and-columns='authors', cross-with='countries',
    method='pearson', shape=(10, 10))

* Results    

>>> cross_corr_matrix.df_.round(3)
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
Table:
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


"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Optional

import pandas as pd

from ._chatbot import format_chatbot_prompt_for_df
from .co_occurrence_matrix import co_occurrence_matrix
from .compute_corr_matrix import compute_corr_matrix
from .cross_correlation_map import cross_correlation_map
from .heat_map import heat_map
from .list_cells_in_matrix import list_cells_in_matrix


# pylint: disable=too-many-instance-attributes
@dataclass
class CrossCorrMatrix:
    """Cross-correlation matrix."""

    #
    # FUNCTION PARAMS:
    rows_and_columns: str
    cross_with: str
    method: str = "pearson"
    #
    # ITEM FILTERS:
    top_n: Optional[int] = None
    occ_range: tuple = (None, None)
    gc_range: tuple = (None, None)
    custom_items: list = datafield(default_factory=list)
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
    metric: str = "CORR"

    def __repr__(self):
        text = "CrossCorrMatrix("
        text += f"rows-and-columns='{self.rows_and_columns}'"
        text += f", cross-with='{self.cross_with}'"
        text += f", method='{self.method}'"
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text

    def list_cells_in_matrix(self):
        """List the cells in the matrix."""
        return list_cells_in_matrix(self)

    def heat_map(self, colormap="Blues"):
        """Plot the cross-correlation matrix as a heat map."""
        return heat_map(self, colormap=colormap)

    def cross_correlation_map(
        self,
        #
        # Map params:
        n_labels=None,
        color="#8da4b4",
        nx_k=None,
        nx_iterations=10,
        nx_random_state=0,
        node_size_min=30,
        node_size_max=70,
        textfont_size_min=10,
        textfont_size_max=20,
        xaxes_range=None,
        yaxes_range=None,
        show_axes=False,
    ):
        return cross_correlation_map(
            cross_corr_matrix=self,
            #
            # Map params:
            n_labels=n_labels,
            color=color,
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


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
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
    """Compute the cross-correlation matrix."""

    def generate_prompt(rows_and_columns, cross_with, corr_matrix):
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
        return format_chatbot_prompt_for_df(
            main_text, corr_matrix.round(3).to_markdown()
        )

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
    )

    corr_matrix = compute_corr_matrix(method, data_matrix)
    prompt = generate_prompt(rows_and_columns, cross_with, corr_matrix)

    return CrossCorrMatrix(
        #
        # PARAMS:
        rows_and_columns=rows_and_columns,
        method=method,
        cross_with=cross_with,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # RESULTS:
        df_=corr_matrix,
        prompt_=prompt,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
