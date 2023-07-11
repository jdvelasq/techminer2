# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _auto_correlation_prompt:

Auto-correlation Prompt
===============================================================================

Returns an auto-correlation prompt.



>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> print(tm2p.auto_correlation_prompt(
...     rows_and_columns='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... ))
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
from ....format_prompt_for_dataframes import format_prompt_for_dataframes
from ..matrix.auto_correlation_matrix import auto_correlation_matrix


def auto_correlation_prompt(
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

    corr_matrix = auto_correlation_matrix(
        #
        # FUNCTION PARAMS:
        rows_and_columns=rows_and_columns,
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
    return format_prompt_for_dataframes(
        main_text, corr_matrix.round(3).to_markdown()
    )
