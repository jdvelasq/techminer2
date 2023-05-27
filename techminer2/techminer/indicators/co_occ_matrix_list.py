"""
Co-ocurrence Matrix List
===============================================================================

Creates a matrix list with all terms of the database, removing the terms in the
stopwords list.


Example
-------

>>> root_dir = "data/regtech/"

>>> from techminer2  import techminer
>>> techminer.indicators.co_occ_matrix_list(
...     'authors', 'keywords', root_dir=root_dir
... ).head(10)
                         row     column  OCC
0             accountability  Brennan R    2
1             accountability    Crane M    2
2             accountability     Ryan P    2
93               charitytech      Lin W    2
94               charitytech    Singh C    2
112               compliance  Brennan R    2
113               compliance    Crane M    2
119               compliance     Ryan P    2
163  data protection officer  Brennan R    2
164  data protection officer    Crane M    2



"""
from ...load_utils import load_stopwords
from ...record_utils import read_records


# pylint: disable=too-many-arguments
# pylint: disable=too-many-statements
def co_occ_matrix_list(
    criterion,
    other_criterion,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a matrix list with all terms of the database.

    Args:
        criterion (str) : column name to be used as column criterion.
        other_criterion (str) : column name to be used as row criterion.
        root_dir (str) : root directory.
        database (str) : database name.
        start_year (int) : start year.
        end_year (int) : end year.
        **filters : filters.

    Returns:
        A dataframe with the matrix list.

    """

    records = read_records(
        root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = records[[criterion]].copy()
    matrix_list = matrix_list.rename(columns={criterion: "column"})
    matrix_list = matrix_list.assign(row=records[[other_criterion]])

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
