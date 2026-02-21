"""
Term Occurrences by Year
===============================================================================

Computes the annual occurrence matrix for the items in a given field.

## >>> from techminer2._core.metrics.term_occurrences_by_year import term_occurrences_by_year
## >>> term_occurrences_by_year(
## ...     field='authors',
## ...     cumulative=False,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/",
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... ).head(10)
year                2015  2016  2017  2018  2019
authors
Almunawar M.N.         0     0     0     0     1
Alt R.                 0     0     0     1     0
Anagnostopoulos I.     0     0     0     1     0
Anshari M.             0     0     0     0     1
Arner D.W.             0     0     1     0     0
Barberis J.            0     0     1     0     0
Beck R.                0     0     0     1     0
Brooks S.              0     0     1     0     0
Brummer C.             0     0     0     0     1
Buchak G.              0     0     0     1     0


"""

from techminer2._internals.mt.mt_global_metrics_by_field_per_year import (
    _mt_global_metrics_by_field_per_year,
)
from techminer2._internals.stopwords import load_user_stopwords


def _mt_term_occurrences_by_year(
    field,
    cumulative,
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    sort_by=None,
    **filters,
):
    """:meta private:"""

    indicators_by_year = _mt_global_metrics_by_field_per_year(
        field=field,
        as_index=True,
        #
        # DATABASE PARAMS
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

    stopwords = load_user_stopwords(root_dir=root_dir)
    indicators_by_year = indicators_by_year.drop(stopwords, axis=0, errors="ignore")

    records = load__filtered_database(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
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
