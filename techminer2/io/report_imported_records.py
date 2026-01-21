"""Report imported records per file"""

import pathlib
import sys

import pandas as pd  # type: ignore


def internal__report_imported_records(root_dir):
    """:meta private:"""

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "data/processed/database.csv.zip",
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    total_records = len(dataframe.index)
    main_records = len(dataframe[dataframe.db_main].index)
    cited_by_records = len(dataframe[dataframe.db_cited_by].index)
    references_records = len(dataframe[dataframe.db_references].index)

    sys.stderr.write(f"INFO: Report\n")
    sys.stderr.write(f"  Total imported records         : {total_records:6d}\n")
    sys.stderr.write(f"  Records in main database       : {main_records:6d}\n")
    sys.stderr.write(f"  Records in cited by database   : {cited_by_records:6d}\n")
    sys.stderr.write(f"  Records in references database : {references_records:6d}\n")
    sys.stderr.flush()
