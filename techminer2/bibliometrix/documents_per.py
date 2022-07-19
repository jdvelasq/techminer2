"""documents by each item in a column"""
from ..read_records import read_records


def documents_per(
    column,
    directory="./",
    database="documents",
):
    """Documents"""

    records = read_records(directory=directory, database=database, use_filter=True)

    records[column] = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()

    records = records[
        [
            column,
            "title",
            "year",
            "source_title",
            "global_citations",
            "local_citations",
            "doi",
        ]
    ]
    records = records.reset_index(drop=True)

    return records
