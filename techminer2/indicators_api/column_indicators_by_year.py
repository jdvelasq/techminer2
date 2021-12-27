"""
Column Indicators by Year
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> column_indicators_by_year(directory, 'authors').head(10)
                       num_documents  ...  local_citations_per_year
authors      pub_year                 ...                          
Dolata M     2016                  1  ...                     1.167
Hong S       2016                  1  ...                     0.167
Hung J-L     2016                  1  ...                     0.667
Kim K        2016                  1  ...                     0.167
Kotarba M    2016                  1  ...                     0.500
Luo B        2016                  1  ...                     0.667
Schueffel P  2016                  1  ...                     2.333
Schwabe G    2016                  1  ...                     1.167
Zavolokina L 2016                  1  ...                     1.167
Brooks S     2017                  1  ...                     3.000
<BLANKLINE>
[10 rows x 6 columns]

"""

import pandas as pd

from ..documents_api.load_filtered_documents import load_filtered_documents


def column_indicators_by_year(directory=None, column="authors"):

    indicators = load_filtered_documents(directory)
    indicators = indicators.assign(num_documents=1)
    indicators[column] = indicators[column].str.split(";")
    indicators = indicators.explode(column)
    indicators[column] = indicators[column].str.strip()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[
        [column, "num_documents", "global_citations", "local_citations", "pub_year"]
    ].copy()
    max_pub_year = indicators.pub_year.max()
    indicators = (
        indicators.groupby([column, "pub_year"], as_index=False)
        .sum()
        .sort_values(by=["pub_year", column], ascending=True)
    )
    indicators["age"] = max_pub_year - indicators.pub_year + 1

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

    index = [
        (name, year) for name, year in zip(indicators[column], indicators.pub_year)
    ]
    index = pd.MultiIndex.from_tuples(index, names=[column, "pub_year"])
    indicators.index = index

    indicators.pop(column)
    indicators.pop("pub_year")

    return indicators
