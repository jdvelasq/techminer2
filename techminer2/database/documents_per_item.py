"""documents by each item in a column"""

from .load.load__database import load__filtered_database


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

    records = load__filtered_database(
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
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
