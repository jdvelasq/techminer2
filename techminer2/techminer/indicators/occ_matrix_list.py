""""
Ocucrrence Matrix List
===============================================================================

"""
from ... import record_utils


def occ_matrix_list(
    column_criterion,
    row_criterion,
    root_dir,
    database,
    start_year,
    end_year,
    **filters,
):
    """Creates a matrix list with all terms of the database.

    Parameters
    ----------
    column_criterion: str
        Criterion to be used to extract the topics.

    row_criterion: str
        Criterion to be used to extract the topics.

    root_dir: str
        Path to the working directory.

    database: str
        Name of the database to be used.

    start_year: int
        Start year to be considered.

    end_year: int
        End year to be considered.

    filters: dict
        Dictionary of filters to be applied to the database.

    Returns
    -------
    pandas.DataFrame



    """

    records = record_utils.read_records(
        root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = records[[column_criterion]].copy()
    matrix_list = matrix_list.rename(columns={column_criterion: "column"})
    matrix_list = matrix_list.assign(row=records[[row_criterion]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(
        ["row", "column"], as_index=False
    ).aggregate("sum")

    return matrix_list
