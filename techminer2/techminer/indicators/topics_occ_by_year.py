"""
Topics Occurrence by Year 
===============================================================================

Computes the annual occurrence matrix of a given criterion.


Examples
--------

>>> root_dir = "data/regtech/"

>>> from techminer2  import techminer
>>> techminer.indicators.topics_occ_by_year(
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

# noqa: W291
"""

from ... import load_utils
from .indicators_by_topic_per_year import indicators_by_topic_per_year


def topics_occ_by_year(
    criterion,
    root_dir="./",
    cumulative=False,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes the annual occurrence matrix of a given criterion.

    The columns are the years, the rows are the criterion values (topics).

    Args:
        criterion (str): criterion to be used as rows.
        root_dir (str, optional): root directory. Defaults to "./".
        cumulative (bool, optional): if True, the matrix is cumulative. Defaults to False.
        database (str, optional): database name. Defaults to "documents".
        start_year (int, optional): start year. Defaults to None.
        end_year (int, optional): end year. Defaults to None.
        filters (dict, optional): filters. Defaults to {}.

    Returns:
        pandas.DataFrame: annual occurrence matrix.

    """

    indicators_by_year = indicators_by_topic_per_year(
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
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

    stopwords = load_utils.load_stopwords(root_dir=root_dir)
    indicators_by_year = indicators_by_year.drop(stopwords, axis=0)

    if cumulative:
        indicators_by_year = indicators_by_year.cumsum(axis=1)

    return indicators_by_year