"""
Column indicators by year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> column_indicators_by_year(
...     'authors',
...     directory=directory, 
... ).head(10)
                  num_documents  ...  local_citations_per_year
authors     year                 ...                          
Arner DW    2016              1  ...                     0.000
Barberis JN 2016              1  ...                     0.000
Baxter LG   2016              1  ...                     0.714
Arner DW    2017              2  ...                     1.167
Barberis JN 2017              2  ...                     1.167
Birch DGW   2017              1  ...                     0.000
Buckley RP  2017              2  ...                     1.167
Chiang K-H  2017              1  ...                     0.000
Huang GKJ   2017              1  ...                     0.000
Huber R     2017              1  ...                     0.000
<BLANKLINE>
[10 rows x 6 columns]

"""
import pandas as pd

from ._read_records import read_records


def column_indicators_by_year(
    column="authors",
    directory="./",
    database="documents",
    use_filter=True,
):
    """Computes column indicators by year."""

    indicators = read_records(
        directory=directory, database=database, use_filter=use_filter
    )
    indicators = indicators.assign(num_documents=1)
    indicators[column] = indicators[column].str.split(";")
    indicators = indicators.explode(column)
    indicators[column] = indicators[column].str.strip()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[
        [column, "num_documents", "global_citations", "local_citations", "year"]
    ].copy()
    max_pub_year = indicators.year.max()
    indicators = (
        indicators.groupby([column, "year"], as_index=False)
        .sum()
        .sort_values(by=["year", column], ascending=True)
    )
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

    indicators["num_documents"] = indicators.num_documents.astype(int)
    indicators["global_citations"] = indicators.global_citations.astype(int)
    indicators["local_citations"] = indicators.local_citations.astype(int)
    indicators = indicators.dropna()

    index = [(name, year) for name, year in zip(indicators[column], indicators.year)]
    index = pd.MultiIndex.from_tuples(index, names=[column, "year"])
    indicators.index = index

    indicators.pop(column)
    indicators.pop("year")

    return indicators
