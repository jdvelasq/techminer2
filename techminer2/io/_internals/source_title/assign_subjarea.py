from functools import lru_cache
from importlib.resources import files
from pathlib import Path

import pandas as pd  # type: ignore

from techminer2 import Field


@lru_cache(maxsize=1)
def _load_subject_areas() -> pd.DataFrame:
    data_path = files("techminer2._internals.package_data.database.data").joinpath(
        "subject_areas.csv"
    )
    return pd.read_csv(str(data_path), encoding="utf-8")


def assign_subjarea(root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if (
        Field.ISSN.value not in dataframe.columns
        and Field.EISSN.value not in dataframe.columns
    ):
        return 0

    subject_areas_df = _load_subject_areas()

    issn_mapping = dict(
        zip(
            subject_areas_df[Field.ISSN.value].dropna(),
            subject_areas_df[Field.SUBJ_AREA.value].dropna(),
        )
    )
    eissn_mapping = dict(
        zip(
            subject_areas_df[Field.EISSN.value].dropna(),
            subject_areas_df[Field.SUBJ_AREA.value].dropna(),
        )
    )

    dataframe[Field.SUBJ_AREA.value] = None

    if Field.ISSN.value in dataframe.columns:
        dataframe[Field.SUBJ_AREA.value] = dataframe[Field.ISSN.value].map(issn_mapping)

    if Field.EISSN.value in dataframe.columns:
        dataframe[Field.SUBJ_AREA.value] = dataframe[Field.SUBJ_AREA.value].fillna(
            dataframe[Field.EISSN.value].map(eissn_mapping)
        )

    non_null_count = int(dataframe[Field.SUBJ_AREA.value].notna().sum())

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
