# flake8: noqa
# pylint: disable=line-too-long
"""
.. _auto_correlation_matrix:

Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.

* Preparation

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p

* Object oriented interface

>>> auto_corr_matrix = (
...     tm2p.records(root_dir=root_dir)
...     .auto_correlation_matrix(
...         rows_and_columns='authors',
...         occ_range=(2, None),
...     )
... )
>>> auto_corr_matrix
AutoCorrMatrix(rows-and-columns='authors', method='pearson', shape=(15,
    15))

* Functional interface

>>> auto_corr_matrix = tm2p.auto_correlation_matrix(
...     rows_and_columns='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> auto_corr_matrix
AutoCorrMatrix(rows-and-columns='authors', method='pearson', shape=(15,
    15))

* Results    
    
>>> auto_corr_matrix.df_.round(3)
                    Arner DW 3:185  ...  Arman AA 2:000
Arner DW 3:185               1.000  ...             0.0
Buckley RP 3:185             1.000  ...             0.0
Barberis JN 2:161            0.787  ...             0.0
Butler T 2:041               0.000  ...             0.0
Hamdan A 2:018               0.000  ...             0.0
Turki M 2:018                0.000  ...             0.0
Lin W 2:017                  0.000  ...             0.0
Singh C 2:017                0.000  ...             0.0
Brennan R 2:014              0.000  ...             0.0
Crane M 2:014                0.000  ...             0.0
Ryan P 2:014                 0.000  ...             0.0
Sarea A 2:012                0.000  ...             0.0
Grassi L 2:002               0.000  ...             0.0
Lanfranchi D 2:002           0.000  ...             0.0
Arman AA 2:000               0.000  ...             1.0
<BLANKLINE>
[15 rows x 15 columns]


>>> print(auto_corr_matrix.prompt_)
Your task is to generate a short paragraph of a research paper analyzing \\
the auto-correlation values between the items of the column 'authors' of a \\
bibliographic dataset.  Analyze the table below which contains the auto- \\
correlation values for the 'authors'. High correlation values indicate that \\
the items tends to appear together in the same document and forms a group. \\
Identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings, in at most 50 words.
<BLANKLINE>
Table:
```
|                    |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Butler T 2:041 |   Hamdan A 2:018 |   Turki M 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |   Ryan P 2:014 |   Sarea A 2:012 |   Grassi L 2:002 |   Lanfranchi D 2:002 |   Arman AA 2:000 |
|:-------------------|-----------------:|-------------------:|--------------------:|-----------------:|-----------------:|----------------:|--------------:|----------------:|------------------:|----------------:|---------------:|----------------:|-----------------:|---------------------:|-----------------:|
| Arner DW 3:185     |            1     |              1     |               0.787 |                0 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                0 |                    0 |                0 |
| Buckley RP 3:185   |            1     |              1     |               0.787 |                0 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                0 |                    0 |                0 |
| Barberis JN 2:161  |            0.787 |              0.787 |               1     |                0 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                0 |                    0 |                0 |
| Butler T 2:041     |            0     |              0     |               0     |                1 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                0 |                    0 |                0 |
| Hamdan A 2:018     |            0     |              0     |               0     |                0 |            1     |           1     |             0 |               0 |                 0 |               0 |              0 |           0.429 |                0 |                    0 |                0 |
| Turki M 2:018      |            0     |              0     |               0     |                0 |            1     |           1     |             0 |               0 |                 0 |               0 |              0 |           0.429 |                0 |                    0 |                0 |
| Lin W 2:017        |            0     |              0     |               0     |                0 |            0     |           0     |             1 |               1 |                 0 |               0 |              0 |           0     |                0 |                    0 |                0 |
| Singh C 2:017      |            0     |              0     |               0     |                0 |            0     |           0     |             1 |               1 |                 0 |               0 |              0 |           0     |                0 |                    0 |                0 |
| Brennan R 2:014    |            0     |              0     |               0     |                0 |            0     |           0     |             0 |               0 |                 1 |               1 |              1 |           0     |                0 |                    0 |                0 |
| Crane M 2:014      |            0     |              0     |               0     |                0 |            0     |           0     |             0 |               0 |                 1 |               1 |              1 |           0     |                0 |                    0 |                0 |
| Ryan P 2:014       |            0     |              0     |               0     |                0 |            0     |           0     |             0 |               0 |                 1 |               1 |              1 |           0     |                0 |                    0 |                0 |
| Sarea A 2:012      |            0     |              0     |               0     |                0 |            0.429 |           0.429 |             0 |               0 |                 0 |               0 |              0 |           1     |                0 |                    0 |                0 |
| Grassi L 2:002     |            0     |              0     |               0     |                0 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                1 |                    1 |                0 |
| Lanfranchi D 2:002 |            0     |              0     |               0     |                0 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                1 |                    1 |                0 |
| Arman AA 2:000     |            0     |              0     |               0     |                0 |            0     |           0     |             0 |               0 |                 0 |               0 |              0 |           0     |                0 |                    0 |                1 |
```
<BLANKLINE>

    

"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Optional

import pandas as pd

from ._chatbot import format_chatbot_prompt_for_df
from .auto_correlation_map import auto_correlation_map
from .compute_corr_matrix import compute_corr_matrix
from .heat_map import heat_map
from .list_cells_in_matrix import list_cells_in_matrix
from .tfidf import tfidf


# pylint: disable=too-many-instance-attributes
@dataclass
class AutoCorrMatrix:
    """Auto-correlation matrix."""

    #
    # FUNCTION PARAMS:
    rows_and_columns: str
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
        text = "AutoCorrMatrix("
        text += f"rows-and-columns='{self.rows_and_columns}'"
        text += f", method='{self.method}'"
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text

    def auto_correlation_map(
        self,
        #
        # FUNCTION PARAMS:
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
        return auto_correlation_map(
            #
            # FUNCTION PARAMS:
            auto_corr_matrix=self,
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

    def list_cells_in_matrix(self):
        """Returns a list of cells in the matrix."""
        return list_cells_in_matrix(self)

    def heat_map(self, colormap="Blues"):
        """Returns a heat map."""
        return heat_map(self, colormap=colormap)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
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
    """Returns an auto-correlation."""

    def generate_prompt(rows_and_columns, corr_matrix):
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
        return format_chatbot_prompt_for_df(
            main_text, corr_matrix.round(3).to_markdown()
        )

    #
    # Main:
    #
    data_matrix = tfidf(
        field=rows_and_columns,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    custom_items = [
        " ".join(col.split(" ")[:-1])
        for col in data_matrix.df_.columns.tolist()
    ]
    corr_matrix = compute_corr_matrix(method=method, data_matrix=data_matrix)
    prompt = generate_prompt(rows_and_columns, corr_matrix)

    return AutoCorrMatrix(
        #
        # PARAMS:
        rows_and_columns=rows_and_columns,
        method=method,
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
