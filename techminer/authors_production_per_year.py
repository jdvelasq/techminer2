"""
Author's production per year
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> authors_production_per_year(directory=directory).head()
         authors  pub_year  ...  num_documents  global_citations_per_year
0         Aas TH      2021  ...              1                        0.0
1     Abakah EJA      2021  ...              1                       17.0
2        Abbas F      2020  ...              1                        2.5
3   Abdullah EME      2018  ...              1                        2.0
4  Abu Daqar MAM      2020  ...              1                        1.0
<BLANKLINE>
[5 rows x 6 columns]

"""

import numpy as np

from .utils import load_filtered_documents


def authors_production_per_year(
    directory="./",
):
    documents = load_filtered_documents(directory=directory)

    columns_to_explode = [
        "authors",
        "global_citations",
        "frac_num_documents",
        "pub_year",
    ]
    indicators = documents[columns_to_explode]
    indicators = indicators.assign(num_documents=1)
    indicators = indicators.assign(authors=indicators.authors.str.split(";"))
    indicators = indicators.explode("authors")
    indicators = indicators.assign(authors=indicators.authors.str.strip())
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.groupby(["authors", "pub_year"], as_index=False).sum()
    indicators = indicators.sort_values(["authors", "pub_year"], ascending=True)

    max_pub_year = documents.pub_year.max()
    indicators["age"] = max_pub_year - indicators.pub_year + 1
    indicators = indicators.assign(
        global_citations_per_year=indicators.global_citations / indicators.age
    )
    indicators.pop("age")

    indicators = indicators.sort_values(["authors", "pub_year"], ascending=True)
    return indicators
