"""Report imported records per file"""

import pathlib
import sys

import pandas as pd  # type: ignore

from ....._internals.log_message import internal__log_message


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

    sys.stderr.write(f"         :   {total_records:6d} total imported records\n")
    sys.stderr.write(f"         :   {main_records:6d} records in main database\n")
    sys.stderr.write(
        f"         :   {cited_by_records:6d} records in cited by database\n"
    )
    sys.stderr.write(
        f"         :   {references_records:6d} records in references database\n"
    )
    sys.stderr.flush()
