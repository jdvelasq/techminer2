from techminer2 import CorpusField
from techminer2._constants import BRITISH_TO_AMERICAN

from ._file_dispatch import get_file_operations
from .data_file import DataFile


def rename_column(
    source: CorpusField,
    target: CorpusField,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    for british, american in BRITISH_TO_AMERICAN.items():
        dataframe[target.value] = dataframe[source.value].str.replace(
            british, american, regex=False
        )

    save_data(df=dataframe, root_directory=root_directory)

    return len(dataframe)
