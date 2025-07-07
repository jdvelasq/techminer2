"""Database file path"""

import pathlib


def internal__get_database_file_path(params):
    """:meta private:"""

    return pathlib.Path(params.root_directory) / "data/processed/database.csv.zip"
