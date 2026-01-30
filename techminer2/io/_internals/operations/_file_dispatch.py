from techminer2._internals.data_access import (
    get_main_data_path,
    get_references_data_path,
    load_main_data,
    load_references_data,
    save_main_data,
    save_references_data,
)

from .data_file import DataFile


def get_file_operations(file: DataFile):
    if file == DataFile.MAIN:
        return (load_main_data, save_main_data, get_main_data_path)
    elif file == DataFile.REFERENCES:
        return (load_references_data, save_references_data, get_references_data_path)
    else:
        raise ValueError(f"Invalid file: {file}")
