"""
Annual Occurrence Matrix
===============================================================================

Computes the annual occurrence matrix of a given criterion.

Examples
--------

>>> directory = "data/regtech/"

>>> from techminer2  import techminer
>>> techminer.indicators.annual_occurrence_matrix('authors',  min_occ=3, directory=directory).head(10)
year        2017  2020
authors               
Arner DW       2     1
Buckley RP     2     1


"""


from .indicators_by_topic import indicators_by_topic
from .indicators_by_topic_per_year import indicators_by_topic_per_year


def annual_occurrence_matrix(
    criterion,
    min_occ=1,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes the annual occurrence matrix of a given criterion.

    The columns are the years, the rows are the criterion values (topics).

    Parameters
    ----------
    criterion : str
        Criterion to be analyzed.

    min_occ : int
        Minimum number of occurrences. Topics with a number of occurrences below are ignored.

    directory : str
        The working directory.

    database : str
        The database name. It can be 'documents', 'cited_by' or 'references'.

    start_year : int
        The start year for filtering the data.

    end_year : int
        The end year for filtering the data.

    filters : dict
        A dictionary of filters. The keys are the field names and the values are the filter values.

    Returns
    -------
    pandas.DataFrame
        The annual occurrence matrix.




    """

    indicators_by_year = indicators_by_topic_per_year(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators = indicators.sort_values("OCC", ascending=False)
    indicators = indicators[indicators["OCC"] >= min_occ]

    indicators_by_year = indicators_by_year.loc[indicators.index,]

    indicators_by_year = indicators_by_year.assign(
        year=indicators_by_year.index.get_level_values("year")
    )
    indicators_by_year.index = indicators_by_year.index.get_level_values(0)

    indicators_by_year = indicators_by_year[["year", "OCC"]]
    indicators_by_year = indicators_by_year.pivot(columns="year")
    indicators_by_year.columns = indicators_by_year.columns.droplevel(0)
    indicators_by_year = indicators_by_year.fillna(0)
    indicators_by_year = indicators_by_year.astype(int)

    return indicators_by_year
