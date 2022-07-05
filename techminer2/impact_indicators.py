"""
Impact Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> impact_indicators("countries", directory=directory).head()
                   OCC  ...  avg_global_citations
countries               ...                      
Australia           14  ...                 16.86
Austria              1  ...                  1.00
Bahrain              8  ...                  2.75
Belgium              1  ...                  0.00
Brunei Darussalam    1  ...                  3.00
<BLANKLINE>
[5 rows x 9 columns]


>>> from pprint import pprint
>>> pprint(sorted(impact_indicators("countries", directory=directory).columns.to_list()))
['OCC',
 'age',
 'avg_global_citations',
 'first_pb_year',
 'g_index',
 'global_citations',
 'global_citations_per_year',
 'h_index',
 'm_index']

"""

import numpy as np
import pandas as pd

from ._read_records import read_records


def impact_indicators(column, directory="./"):
    """
    Impact index analysis

    Parameters
    ----------
    directory_or_records: str
        Directory or pandas dataframe with records.
    column: str
        Name of the column to analyze
    stopwords: list
        List of stopwords to remove from the analysis.

    Returns
    -------
    impact_analysis: pandas.DataFrame
        Impact analysis of the column
    """

    documents = read_records(
        directory=directory, database="documents", use_filter=False
    )

    if column not in [
        "authors",
        "authors_id",
        "countries",
        "institutions",
        "source_title",
        "source_abbr",
    ]:
        raise ValueError(
            'Impact indicators only works with "authors", "authors_id", "countries", "institutions", "source_title" or "source_abbr".'
        )

    columns_to_explode = [
        column,
        "global_citations",
        "year",
    ]
    detailed_citations = documents[columns_to_explode]
    detailed_citations[column] = detailed_citations[column].str.split(";")
    detailed_citations = detailed_citations.explode(column)
    detailed_citations[column] = detailed_citations[column].str.strip()
    detailed_citations = detailed_citations.reset_index(drop=True)
    detailed_citations = detailed_citations.assign(
        cumcount_=detailed_citations.sort_values("global_citations", ascending=False)
        .groupby(column)
        .cumcount()
        + 1
    )
    detailed_citations = detailed_citations.sort_values(
        [column, "global_citations", "cumcount_"], ascending=[True, False, True]
    )
    detailed_citations = detailed_citations.assign(
        cumcount_2=detailed_citations.cumcount_.map(lambda w: w * w)
    )

    detailed_citations["first_pb_year"] = detailed_citations.groupby(column)[
        "year"
    ].transform("min")

    detailed_citations["age"] = (
        documents.year.max() - detailed_citations["first_pb_year"] + 1
    )
    ages = detailed_citations.groupby(column, as_index=True).agg({"age": np.max})

    global_citations = detailed_citations.groupby(column, as_index=True).agg(
        {"global_citations": np.sum}
    )

    first_pb_year = detailed_citations.groupby(column, as_index=True).agg(
        {"first_pb_year": np.min}
    )

    occ = detailed_citations.groupby(column, as_index=True).size()

    h_indexes = detailed_citations.query("global_citations >= cumcount_")
    h_indexes = h_indexes.groupby(column, as_index=True).agg({"cumcount_": np.max})
    h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})

    g_indexes = detailed_citations.query("global_citations >= cumcount_2")
    g_indexes = g_indexes.groupby(column, as_index=True).agg({"cumcount_": np.max})
    g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})

    indicators = pd.concat(
        [occ, global_citations, first_pb_year, ages, h_indexes, g_indexes],
        axis=1,
        sort=False,
    )

    indicators = indicators.rename(columns={0: "OCC"})
    indicators = indicators.fillna(0)

    indicators = indicators.assign(m_index=indicators.h_index / indicators.age)
    indicators["m_index"] = indicators.m_index.round(decimals=2)

    indicators = indicators.assign(
        global_citations_per_year=indicators.global_citations / indicators.age
    )
    indicators = indicators.assign(
        avg_global_citations=indicators.global_citations / indicators.OCC
    )

    indicators[
        "global_citations_per_year"
    ] = indicators.global_citations_per_year.round(decimals=2)

    indicators["avg_global_citations"] = indicators.avg_global_citations.round(
        decimals=2
    )

    indicators["h_index"] = indicators["h_index"].astype(int)
    indicators["g_index"] = indicators["g_index"].astype(int)
    indicators["age"] = indicators["age"].astype(int)

    # indicators = indicators.sort_values("h_index", ascending=False)
    indicators = indicators.sort_index(axis="index")
    indicators.first_pb_year = indicators.first_pb_year.astype(int)

    return indicators
