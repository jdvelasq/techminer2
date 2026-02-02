import pandas as pd  # type: ignore

from techminer2 import Field

from ._file_dispatch import get_file_operations
from .data_file import DataFile


def _extract_uppercase_words_and_np(text):
    if pd.isna(text):
        return pd.NA
    words = [word for word in str(text).split() if word.isupper()]
    return "; ".join(words) if words else pd.NA


def extract_uppercase(
    source: Field,
    target: Field,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    dataframe[target.value] = dataframe[source.value].apply(
        _extract_uppercase_words_and_np
    )

    save_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[target.value].notna().sum())
