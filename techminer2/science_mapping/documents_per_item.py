"""documents by each item in a column"""
from ..read_records import read_records


def documents_per_item(
    field,
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """Documents"""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records[field] = records[field].str.split(";")
    records = records.explode(field)
    records[field] = records[field].str.strip()

    records = records[
        [
            field,
            "document_title",
            "year",
            "source_title",
            "global_citations",
            "local_citations",
            "doi",
        ]
    ]
    records = records.reset_index(drop=True)

    return records
