"""
Impact Analysis
===============================================================================

"""

import numpy as np
import pandas as pd

from .term_analysis import count_documents_by_term, count_global_citations_by_term
from .utils import explode, load_records, load_stopwords


def _impact_analysis_from_records(records, column, stopwords=None):

    if column not in [
        "authors",
        "authors_id",
        "countries",
        "institutions",
    ]:
        raise ValueError(
            "Impact analysis only works with 'authors', 'authors_id', 'countries' or 'institutions'."
        )

    records = records.copy()
    stopwords = load_stopwords(stopwords)

    columns_to_explode = [
        column,
        "global_citations",
    ]
    detailed_citations = records[columns_to_explode]
    detailed_citations = explode(detailed_citations[columns_to_explode], column)
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

    age = records[
        [
            column,
            "pub_year",
        ]
    ]
    age = explode(age, column)
    age = (
        age.groupby(column, as_index=True)
        .agg({"pub_year": np.min})
        .rename(columns={"pub_year": "age"})
    )
    age = records.pub_year.max() - age.age + 1

    num_documents = count_documents_by_term(records, column)
    num_global_citations = count_global_citations_by_term(records, column)

    impact = pd.concat(
        [h_indexes, g_indexes, age, num_documents, num_global_citations],
        axis=1,
        sort=False,
    )

    impact = impact.assign(m_index=impact.h_index / impact.age)
    impact = impact.assign(
        global_citations_per_year=impact.global_citations / impact.age
    )
    impact = impact.assign(
        avg_global_citations=impact.global_citations / impact.num_documents
    )

    impact = impact.fillna(0)

    impact["m_index"] = impact.m_index.round(decimals=2)
    impact["global_citations_per_year"] = impact.global_citations_per_year.round(
        decimals=2
    )
    impact["avg_global_citations"] = impact.avg_global_citations.round(decimals=2)

    impact = impact.drop(columns=["age"])

    impact["h_index"] = impact["h_index"].astype(int)
    impact["g_index"] = impact["g_index"].astype(int)

    return impact


def _impact_analysis_from_directory(directory, column, stopwords):
    return _impact_analysis_from_records(
        records=load_records(directory),
        column=column,
        stopwords=stopwords,
    )


def impact_analysis(directory_or_records, column, stopwords=None):
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
    if isinstance(directory_or_records, str):
        return _impact_analysis_from_directory(
            directory=directory_or_records,
            column=column,
            stopwords=stopwords,
        )

    elif isinstance(directory_or_records, pd.DataFrame):
        return _impact_analysis_from_records(
            records=directory_or_records,
            column=column,
            stopwords=stopwords,
        )

    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
