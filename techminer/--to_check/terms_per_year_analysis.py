"""
Terms per year analysis
===============================================================================
"""
import numpy as np
import pandas as pd

from techminer.terms_analysis import count_documents_by_term

from .utils import adds_counters_to_axis, explode, load_filtered_documents


def terms_per_year_analysis(
    directory,
    column,
    metric="num_documents",
    sep="; ",
    min_occ=None,
):
    documents = load_filtered_documents(directory)
    documents = documents.assign(num_documents=1)
    exploded = explode(
        documents[
            [
                "pub_year",
                column,
                "num_documents",
                "local_citations",
                "global_citations",
                "document_id",
            ]
        ],
        column,
        sep,
    )

    #  conteo y seleccion por minima ocurrencia
    total_documents = exploded.groupby(column)["num_documents"].transform("sum")
    exploded = exploded.assign(total_documents=total_documents)
    exploded = exploded[exploded.total_documents >= min_occ]

    table = exploded.groupby([column, "pub_year"], as_index=False).agg(
        {
            "num_documents": np.sum,
            "local_citations": np.sum,
            "global_citations": np.sum,
        }
    )

    table = table[["pub_year", column, metric]].copy()

    table = table.pivot(
        values=metric,
        index="pub_year",
        columns=column,
    )
    table = table.fillna(0)

    table = adds_counters_to_axis(
        documents, table, axis="columns", column=column, sep="; "
    )

    table = adds_counters_to_axis(
        documents, table, axis="index", column="pub_year", sep=None
    )

    table = table.sort_index(level=1, axis="columns", ascending=False)
    table = table.astype(int)

    return table
