"""documents by each item in a column"""
from .._read_records import read_records


def bibliometrix__documents_per(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Documents"""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records[criterion] = records[criterion].str.split(";")
    records = records.explode(criterion)
    records[criterion] = records[criterion].str.strip()

    records = records[
        [
            criterion,
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
