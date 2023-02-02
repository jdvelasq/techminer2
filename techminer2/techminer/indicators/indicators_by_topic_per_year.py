"""
Bibliometric Indicators by Topic per Year
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2  import techminer
>>> techminer.indicators.indicators_by_topic_per_year(
...     'authors',
...     directory=directory,
... ).head(20)
a                        OCC  ...  local_citations_per_year
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
>>> pprint(sorted(techminer.indicators.indicators_by_topic_per_year('authors',directory=directory).columns.to_list()))
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


def indicators_by_topic_per_year(
    criterion="authors",
    directory="./",
    database="documents",
    as_index=True,
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes indicators by topic per year."""

    indicators = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators.assign(OCC=1)
    indicators[criterion] = indicators[criterion].str.split(";")
    indicators = indicators.explode(criterion)
    indicators[criterion] = indicators[criterion].str.strip()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[
        [criterion, "OCC", "global_citations", "local_citations", "year"]
    ].copy()
    indicators = indicators.dropna()
    max_pub_year = indicators.year.max()
    indicators = (
        indicators.groupby([criterion, "year"], as_index=False)
        .sum()
        .sort_values(by=["year", criterion], ascending=True)
    )
    indicators = indicators.sort_values([criterion, "year"], ascending=True)

    indicators["cum_OCC"] = indicators.groupby([criterion]).OCC.cumsum()

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

    indicators = indicators.sort_values(by=[criterion, "year"], ascending=True)

    if as_index is False:
        return indicators

    index = [(name, year) for name, year in zip(indicators[criterion], indicators.year)]
    index = pd.MultiIndex.from_tuples(index, names=[criterion, "year"])
    indicators.index = index

    indicators.pop(criterion)
    indicators.pop("year")

    return indicators
