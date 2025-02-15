"""Report imported records per file"""

import pathlib
import sys

import pandas as pd  # type: ignore

from .....internals.log_info_message import log_info_message


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

    sys.stderr.write(f"        :   Total imported records: {total_records:6d}\n")
    sys.stderr.write(f"        :             Main records: {main_records:6d}\n")
    sys.stderr.write(f"        :         Cited by records: {cited_by_records:6d}\n")
    sys.stderr.write(f"        :       References records: {references_records:6d}\n")
    sys.stderr.flush()
