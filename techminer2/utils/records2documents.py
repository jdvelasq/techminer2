import pandas as pd


def records2documents(
    matrix,
    documents,
):

    matrix = matrix.copy()

    # -------------------------------------------------------------------------

    records2ids = dict(
        zip(documents.record_no, documents.document_id),
    )

    records2global_citations = dict(
        zip(documents.record_no, documents.global_citations)
    )

    records2local_citations = dict(
        zip(documents.record_no, documents.local_citations),
    )

    # -------------------------------------------------------------------------

    new_indexes = matrix.columns.get_level_values(0)

    new_indexes = [
        (
            records2ids[index],
            records2global_citations[index],
            records2local_citations[index],
        )
        for index in new_indexes
    ]

    new_indexes = pd.MultiIndex.from_tuples(
        new_indexes, names=["document", "global_citations", "local_citations"]
    )

    # -------------------------------------------------------------------------

    matrix.columns = new_indexes.copy()
    matrix.index = new_indexes.copy()

    # -------------------------------------------------------------------------

    return matrix
