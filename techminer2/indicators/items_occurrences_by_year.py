# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Items Occurrence by Year 
===============================================================================

Computes the annual occurrence matrix for the items in a given field.


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.metrics.items_occ_by_year(
...     'authors',  root_dir=root_dir
... ).head(10)
year               2016  2017  2018  2019  2020  2021  2022  2023
authors                                                          
Abdullah Y            0     0     0     0     0     0     1     0
Ajmi JA               0     0     0     0     0     1     0     0
Anagnostopoulos I     0     0     1     0     0     0     0     0
Anasweh M             0     0     0     0     1     0     0     0
Arman AA              0     0     0     0     0     0     2     0
Arner DW              0     2     0     0     1     0     0     0
Barberis JN           0     2     0     0     0     0     0     0
Battanta L            0     0     0     0     1     0     0     0
Baxter LG             1     0     0     0     0     0     0     0
Becker M              0     0     0     0     1     0     0     0


"""
from .._common._stopwords_lib import load_stopwords
from .._read_records import read_records
from .global_metrics_by_field_per_year import global_metrics_by_field_per_year


# pylint: disable=too-many-arguments
def items_occurrences_by_year(
    #
    # FUNCTION PARAMS:
    field,
    cumulative=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes the annual occurrence matrix of a given field.

    The columns are the years, the rows are the criterion values (field).

    Args:
        field (str): field to be used as rows.
        root_dir (str, optional): root directory. Defaults to "./".
        cumulative (bool, optional): if True, the matrix is cumulative. Defaults to False.
        database (str, optional): database name. Defaults to "documents".
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        pandas.DataFrame: annual occurrence matrix.

    # pylint: disable=line-too-long
    """

    indicators_by_year = global_metrics_by_field_per_year(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators_by_year = indicators_by_year.assign(
        year=indicators_by_year.index.get_level_values("year")
    )
    indicators_by_year.index = indicators_by_year.index.get_level_values(0)

    indicators_by_year = indicators_by_year[["year", "OCC"]]
    indicators_by_year = indicators_by_year.pivot(columns="year")
    indicators_by_year.columns = indicators_by_year.columns.droplevel(0)
    indicators_by_year = indicators_by_year.fillna(0)
    indicators_by_year = indicators_by_year.astype(int)

    stopwords = load_stopwords(root_dir=root_dir)
    indicators_by_year = indicators_by_year.drop(stopwords, axis=0, errors="ignore")

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    year_min = records.year.min()
    year_max = records.year.max()
    for year in range(year_min, year_max + 1):
        if year not in indicators_by_year.columns:
            indicators_by_year[year] = 0

    indicators_by_year = indicators_by_year.sort_index(axis=1)

    if cumulative:
        indicators_by_year = indicators_by_year.cumsum(axis=1)

    return indicators_by_year
