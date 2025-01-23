"""Report imported records per file"""

import pathlib

import pandas as pd  # type: ignore

from ...message import message


def internal__report_imported_records(root_dir):
    """:meta private:"""

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    total_records = len(dataframe.index)
    main_records = len(dataframe[dataframe.db_main].index)
    cited_by_records = len(dataframe[dataframe.db_cited_by].index)
    references_records = len(dataframe[dataframe.db_references].index)

    message(f"Total imported records: {total_records}")
    message(f"          Main records:    {main_records}")
    message(f"      Cited by records:    {cited_by_records}")
    message(f"    References records:    {references_records}")
