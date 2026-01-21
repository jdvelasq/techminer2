from importlib.resources import files
from pathlib import Path

import pandas as pd  # type: ignore

_SUBJECT_AREAS_CACHE = None


def _load_subject_areas() -> pd.DataFrame:
    global _SUBJECT_AREAS_CACHE
    if _SUBJECT_AREAS_CACHE is None:
        data_path = files(
            "techminer2.scopus._internals.bibliographical_information.data"
        ).joinpath("subject_areas.csv")
        _SUBJECT_AREAS_CACHE = pd.read_csv(str(data_path), encoding="utf-8")
    return _SUBJECT_AREAS_CACHE


def normalize_subject_areas(
    issn_column: str,
    eissn_column: str,
    target: str,
    root_directory: str,
) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
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

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())
