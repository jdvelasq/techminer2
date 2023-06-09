# flake8: noqa
"""
Co-ocurrence Matrix List
===============================================================================

Creates a matrix list with all terms of the database, removing the terms in the
stopwords list.


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2  import techminer
>>> techminer.indicators.co_occ_matrix_list(
...     columns='authors', rows='keywords', root_dir=root_dir
... ).head(10)
                         row     column  OCC
0             ACCOUNTABILITY  Brennan R    2
1             ACCOUNTABILITY    Crane M    2
2             ACCOUNTABILITY     Ryan P    2
98                COMPLIANCE  Brennan R    2
99                COMPLIANCE    Crane M    2
101               COMPLIANCE     Ryan P    2
149  DATA_PROTECTION_OFFICER  Brennan R    2
150  DATA_PROTECTION_OFFICER    Crane M    2
151  DATA_PROTECTION_OFFICER     Ryan P    2
206                  FINANCE   Arman AA    2


# pylint: disable=line-too-long
"""
from ...load_utils import load_stopwords
from ...record_utils import read_records


# pylint: disable=too-many-arguments
# pylint: disable=too-many-statements
def co_occ_matrix_list(
    columns,
    rows,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Creates a matrix list with all terms of the database.

    Args:
        columns (str) : column name to be used as column criterion.
        rows (str) : column name to be used as row criterion.
        root_dir (str) : root directory.
        database (str) : database name.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.


    Returns:
        A dataframe with the matrix list.

    # pylint: disable=line-too-long
    """

    records = read_records(
        # Database params:
        root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_list = records[[columns]].copy()
    matrix_list = matrix_list.rename(columns={columns: "column"})
    matrix_list = matrix_list.assign(row=records[[rows]])

    stopwords = load_stopwords(root_dir=root_dir)

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()
        matrix_list = matrix_list[~matrix_list[name].isin(stopwords)]

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(
        ["row", "column"], as_index=False
    ).aggregate("sum")

    matrix_list = matrix_list.sort_values(
        ["OCC", "row", "column"], ascending=[False, True, True]
    )

    return matrix_list
