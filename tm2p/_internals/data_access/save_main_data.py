"""
Smoke test:
    >>> from techminer2.database._internals.io import internal__write_records_to_database
    >>> internal__write_records_to_database(params, records) # doctest: +SKIP


"""

import pandas as pd

from tm2p._internals.data_access.get_main_data_path import get_main_data_path

from .get_main_data_path import get_main_data_path


def save_main_data(df: pd.DataFrame, root_directory: str) -> None:

    main_data_path = get_main_data_path(root_directory)

    temp_file = main_data_path.with_suffix(".tmp")
    df.to_csv(
        temp_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
    temp_file.replace(main_data_path)
