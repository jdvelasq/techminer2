"""
This function selects a subset of columns from a dataframe of performance metrics by an specific metric.

"""


def select_record_columns_by_metric(
    records,
    metric,
):
    """:meta private:"""

    if metric == "OCCGC":
        columns = [
            "rank_occ",
            "rank_gcs",
            "rank_lcs",
            "OCC",
            "global_citations",
            "local_citations",
            "h_index",
            "g_index",
            "m_index",
        ]

    if metric == "OCC":
        #
        between = [_ for _ in records.columns if _.startswith("between")]
        if len(between) > 0:
            between = between[0]
        else:
            between = None
        #
        before = [_ for _ in records.columns if _.startswith("before")]
        if len(before) > 0:
            before = before[0]
        else:
            before = None
        #
        columns = [
            "rank_occ",
            "OCC",
        ]
        #
        if between is not None:
            columns += [between]
        if before is not None:
            columns += [before]
        if "growth_percentage" in records.columns:
            columns += ["growth_percentage"]
        if "average_growth_rate" in records.columns:
            columns += ["average_growth_rate"]
        if "average_docs_per_year" in records.columns:
            columns += ["average_docs_per_year"]

    if metric in [
        "global_citations",
        "local_citations",
    ]:
        columns = [
            "rank_gcs",
            "rank_lcs",
            "global_citations",
            "local_citations",
            "global_citations_per_document",
            "local_citations_per_document",
            "global_citations_per_year",
        ]

    if metric in [
        "h_index",
        "g_index",
        "m_index",
    ]:
        columns = [
            "h_index",
            "g_index",
            "m_index",
        ]

    return records[columns]
