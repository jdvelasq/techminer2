# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _cross_correlation_prompt:

Cross-correlation Prompt
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> print(tm2p.cross_correlation_prompt(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... ))
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

from ....format_prompt_for_dataframes import format_prompt_for_dataframes
from ..matrix.co_occurrence_matrix import co_occurrence_matrix
from ..matrix.compute_corr_matrix import compute_corr_matrix
from ..matrix.cross_correlation_matrix import cross_correlation_matrix
from ..matrix.heat_map import heat_map

# from ..matrix.list_cells_in_matrix import list_cells_in_matrix
from .cross_correlation_map import cross_correlation_map


def cross_correlation_prompt(
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

    corr_matrix = cross_correlation_matrix(
        #
        # FUNCTION PARAMS:
        rows_and_columns=rows_and_columns,
        cross_with=cross_with,
        method=method,
        #
        # ITEM PARAMS:
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
    return format_prompt_for_dataframes(
        main_text, corr_matrix.round(3).to_markdown()
    )
