"""documents by each item in a column"""
from ..._read_records import read_records


def documents_per_item(
    field,
    root_dir="./",
    database="main",
    #
    # DATABASE PARAMS:
    year_filter=None,
    cited_by_filter=None,
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
