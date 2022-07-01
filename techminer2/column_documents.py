"""documents by each item in a column"""
from ._read_records import read_records


def column_documents(
    column,
    directory="./",
    database="documents",
):
    """Column documents"""

    records = read_records(directory=directory, database=database, use_filter=True)

    records[column] = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()

    records = records[
        [
            column,
            "title",
            "source_title",
            "global_citations",
            "local_citations",
            "document_id",
        ]
    ]
    records = records.reset_index(drop=True)

    return records
