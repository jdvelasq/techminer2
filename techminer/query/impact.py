"""
Impact analysis
================

"""

import numpy as np
from techminer.data import load_records, load_stopwords
from techminer.utils import explode


def compute_h_and_g_index(records, column):
    """
    Compute the h-index of a column

    """
    citations = records[[column, "global_citations", "record_id"]].copy()
    citations = (
        records.assign(
            rn=records.sort_values("global_citations", ascending=False)
            .groupby(column)
            .cumcount()
            + 1
        )
    ).sort_values([column, "global_citations", "rn"], ascending=[False, False, True])
    citations["rn2"] = citations.rn.map(lambda w: w * w)

    h_values = citations.query("global_citations >= rn")
    h_values = h_values.groupby(column, as_index=False).agg({"rn": np.max})
    h_dict = {key: value for key, value in zip(h_values[column], h_values.rn)}

    g_values = citations.query("global_citations >= rn2")
    g_values = g_values.groupby(column, as_index=False).agg({"rn": np.max})
    g_dict = {key: value for key, value in zip(g_values[column], g_values.rn)}

    return h_dict, g_dict


def compute_impact_index(directory_or_records, column, stopwords=None):
    """
    Impact analysis

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

    if column not in ["authors", "countries", "institutions"]:
        raise ValueError(
            "Impact analysis only works with 'authors', 'countries' or 'institutions'"
        )

    records = load_records(directory_or_records)
    stopwords = load_stopwords(stopwords)

    records = records.copy()
    records = records.assign(first_year=records.pub_year)
    records = records.assign(num_documents=1)
    records = records.assign(
        frac_num_documents=records.frac_num_documents.map(
            lambda w: round(w, 2), na_action="ignore"
        )
    )
    if column == "authors":
        columns_to_explode = [
            column,
            "frac_num_documents",
            "num_documents",
            "global_citations",
            "first_year",
            "record_id",
        ]

        agg = {
            "frac_num_documents": np.sum,
            "num_documents": np.sum,
            "global_citations": np.sum,
            "first_year": np.min,
        }
    else:
        columns_to_explode = [
            column,
            "num_documents",
            "global_citations",
            "first_year",
            "record_id",
        ]
        agg = {
            "num_documents": np.sum,
            "global_citations": np.sum,
            "first_year": np.min,
        }
    exploded_records = explode(records[columns_to_explode], column)
    result = exploded_records.groupby(column, as_index=False).agg(agg)
    result = result.assign(last_year=records.pub_year.max())
    result = result.assign(years=result.last_year - result.first_year + 1)
    result = result.assign(
        global_citations_per_year=result.global_citations / result.years
    )
    result["global_citations_per_year"] = result.global_citations_per_year.map(
        lambda w: round(w, 2)
    )
    result = result.assign(
        avg_global_citations=result.global_citations / result.num_documents
    )
    result["avg_global_citations"] = result.avg_global_citations.map(
        lambda w: round(w, 2)
    )
    result["global_citations"] = result.global_citations.astype(int)

    #
    # Indice H
    #
    h_dict, g_dict = compute_h_and_g_index(records, column)
    result = result.assign(h_index=result[column].map(h_dict))
    result = result.assign(m_index=result.h_index / result.years)
    result["m_index"] = result["m_index"].map(lambda w: round(w, 2))
    result = result.assign(g_index=result[column].map(g_dict))

    ## limit to / exclude options
    # result = exclude_terms(data=result, axis=0)

    return result
