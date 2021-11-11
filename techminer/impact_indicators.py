"""
Impact indicators
===============================================================================



>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> impact_indicators(directory, "countries").head()
                h_index  g_index  num_documents  global_citations  m_index  \\
united states        23        7            187              1614     3.29   
china                18        6            186              1159     2.25   
united kingdom       16        6            148              1081     2.29   
south korea          13        6             65               754     1.62   
germany              12        5             61               626     1.71   
.
                global_citations_per_year  avg_global_citations  
united states                      230.57                  8.63  
china                              144.88                  6.23  
united kingdom                     154.43                  7.30  
south korea                         94.25                 11.60  
germany                             89.43                 10.26

"""

import numpy as np
import pandas as pd

from .column_indicators import column_indicators
from .utils import explode, load_filtered_documents, load_stopwords


def impact_indicators(directory, column, sep="; "):
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

    documents = load_filtered_documents(directory)

    if column not in [
        "authors",
        "authors_id",
        "countries",
        "institutions",
    ]:
        raise ValueError(
            "Impact indicators only works with 'authors', 'authors_id', 'countries' or 'institutions'."
        )

    columns_to_explode = [
        column,
        "global_citations",
    ]
    detailed_citations = documents[columns_to_explode]
    detailed_citations = explode(detailed_citations[columns_to_explode], column, sep)
    detailed_citations = detailed_citations.assign(
        cumcount_=detailed_citations.sort_values("global_citations", ascending=False)
        .groupby(column)
        .cumcount()
        + 1
    )
    detailed_citations = detailed_citations.sort_values(
        [column, "global_citations", "cumcount_"], ascending=[False, False, True]
    )
    detailed_citations = detailed_citations.assign(
        cumcount_2=detailed_citations.cumcount_.map(lambda w: w * w)
    )

    h_indexes = detailed_citations.query("global_citations >= cumcount_")
    h_indexes = h_indexes.groupby(column, as_index=True).agg({"cumcount_": np.max})
    h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})

    g_indexes = detailed_citations.query("global_citations >= cumcount_2")
    g_indexes = g_indexes.groupby(column, as_index=True).agg({"cumcount_": np.max})
    g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})

    age = documents[
        [
            column,
            "pub_year",
        ]
    ]
    age = explode(age, column, sep)
    age = (
        age.groupby(column, as_index=True)
        .agg({"pub_year": np.min})
        .rename(columns={"pub_year": "age"})
    )
    age = documents.pub_year.max() - age.age + 1

    column_indicators_ = column_indicators(directory=directory, column=column, sep=sep)

    num_documents = column_indicators_.num_documents
    global_citations = column_indicators_.global_citations

    indicators = pd.concat(
        [h_indexes, g_indexes, age, num_documents, global_citations],
        axis=1,
        sort=False,
    )

    indicators = indicators.assign(m_index=indicators.h_index / indicators.age)
    indicators = indicators.assign(
        global_citations_per_year=indicators.global_citations / indicators.age
    )
    indicators = indicators.assign(
        avg_global_citations=indicators.global_citations / indicators.num_documents
    )

    indicators = indicators.fillna(0)

    indicators["m_index"] = indicators.m_index.round(decimals=2)
    indicators[
        "global_citations_per_year"
    ] = indicators.global_citations_per_year.round(decimals=2)
    indicators["avg_global_citations"] = indicators.avg_global_citations.round(
        decimals=2
    )

    indicators = indicators.drop(columns=["age"])

    indicators["h_index"] = indicators["h_index"].astype(int)
    indicators["g_index"] = indicators["g_index"].astype(int)

    indicators = indicators.sort_values("h_index", ascending=False)

    return indicators
