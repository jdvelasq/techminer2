# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Global Indicators by Field per Year 
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2 as tm2
>>> tm2.global_indicators_by_field_per_year(
...     'authors',
...     root_dir=root_dir,
... ).head(20)
                        OCC  ...  local_citations_per_year
authors           year       ...                          
Abdullah Y        2022    1  ...                     0.000
Ajmi JA           2021    1  ...                     0.333
Anagnostopoulos I 2018    1  ...                     2.833
Anasweh M         2020    1  ...                     1.000
Arman AA          2022    2  ...                     0.000
Arner DW          2017    2  ...                     0.429
                  2020    1  ...                     1.250
Barberis JN       2017    2  ...                     0.429
Battanta L        2020    1  ...                     0.000
Baxter LG         2016    1  ...                     0.000
Becker M          2020    1  ...                     0.750
Beheshti A/1      2021    1  ...                     0.000
Boitan IA         2020    1  ...                     0.000
Boticiu SR        2023    1  ...                     0.000
Brand V           2020    1  ...                     0.750
Brennan R         2020    1  ...                     0.750
                  2021    1  ...                     0.000
Breymann W        2018    1  ...                     1.333
Brooks R          2018    1  ...                     0.833
Buchkremer R      2020    1  ...                     0.750
<BLANKLINE>
[20 rows x 7 columns]


>>> from pprint import pprint
>>> pprint(
...     sorted(
...         tm2p.global_indicators_by_field_per_year(
...             'authors', root_dir=root_dir).columns.to_list()
...     )
... )
['OCC',
 'age',
 'cum_OCC',
 'global_citations',
 'global_citations_per_year',
 'local_citations',
 'local_citations_per_year']

"""
import pandas as pd

from ..._read_records import read_records


def global_indicators_by_field_per_year(
    field,
    as_index=True,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes bibliometric indicators by topic per year.

    Args:
        field (str): column name to be used as criterion.
        root_dir (str): root directory.
        database (str): database name.
        as_index (bool): if True, the criterion is used as index.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        pandas.DataFrame: a dataframe containing the indicators.

    # pylint: disable=line-too-long
    """
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = records.assign(OCC=1)
    indicators[field] = indicators[field].str.split(";")
    indicators = indicators.explode(field)
    indicators[field] = indicators[field].str.strip()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[
        [field, "OCC", "global_citations", "local_citations", "year"]
    ].copy()
    indicators = indicators.dropna()
    max_pub_year = indicators.year.max()
    indicators = (
        indicators.groupby([field, "year"], as_index=False)
        .sum()
        .sort_values(by=["year", field], ascending=True)
    )
    indicators = indicators.sort_values([field, "year"], ascending=True)

    indicators["cum_OCC"] = indicators.groupby([field]).OCC.cumsum()

    indicators.insert(3, "cum_OCC", indicators.pop("cum_OCC"))

    indicators["age"] = max_pub_year - indicators.year + 1

    indicators = indicators.assign(
        global_citations_per_year=indicators.global_citations / indicators.age
    )

    indicators = indicators.assign(
        local_citations_per_year=indicators.local_citations / indicators.age
    )

    indicators["global_citations_per_year"] = indicators[
        "global_citations_per_year"
    ].round(3)
    indicators["local_citations_per_year"] = indicators[
        "local_citations_per_year"
    ].round(3)

    indicators["OCC"] = indicators.OCC.astype(int)
    indicators["cum_OCC"] = indicators.cum_OCC.astype(int)
    indicators["global_citations"] = indicators.global_citations.astype(int)
    indicators["local_citations"] = indicators.local_citations.astype(int)
    # indicators = indicators.dropna()

    indicators = indicators.sort_values(by=[field, "year"], ascending=True)

    if as_index is False:
        return indicators

    # index = [
    #     (name, year)
    #     for name, year in zip(indicators[criterion], indicators.year)
    # ]
    index = list(zip(indicators[field], indicators.year))

    index = pd.MultiIndex.from_tuples(index, names=[field, "year"])
    indicators.index = index

    indicators.pop(field)
    indicators.pop("year")

    return indicators
