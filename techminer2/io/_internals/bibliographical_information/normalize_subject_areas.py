from functools import lru_cache
from importlib.resources import files
from pathlib import Path

import pandas as pd  # type: ignore


@lru_cache(maxsize=1)
def _load_subject_areas() -> pd.DataFrame:
    data_path = files("techminer2._internals.package_data.database.data").joinpath(
        "subject_areas.csv"
    )
    return pd.read_csv(str(data_path), encoding="utf-8")


def normalize_subject_areas(
    issn_column: str,
    eissn_column: str,
    target: str,
    root_directory: str,
) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if issn_column not in dataframe.columns and eissn_column not in dataframe.columns:
        return 0

    subject_areas_df = _load_subject_areas()

    issn_mapping = dict(
        zip(
            subject_areas_df["issn"].dropna(),
            subject_areas_df["subject_areas"].dropna(),
        )
    )
    eissn_mapping = dict(
        zip(
            subject_areas_df["eissn"].dropna(),
            subject_areas_df["subject_areas"].dropna(),
        )
    )

    dataframe[target] = None

    if issn_column in dataframe.columns:
        dataframe[target] = dataframe[issn_column].map(issn_mapping)

    if eissn_column in dataframe.columns:
        dataframe[target] = dataframe[target].fillna(
            dataframe[eissn_column].map(eissn_mapping)
        )

    non_null_count = int(dataframe[target].notna().sum())

    temp_file = database_file.with_suffix(".tmp")
    dataframe.to_csv(
        temp_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
    temp_file.replace(database_file)

    return non_null_count
