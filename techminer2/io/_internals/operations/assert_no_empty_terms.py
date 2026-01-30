# CODE_REVIEW: 2025-01-27

from techminer2 import Field
from techminer2._internals.data_access import load_main_data


def assert_no_empty_terms(
    source: Field,
    root_directory: str = "./",
) -> None:

    assert isinstance(source, Field)
    assert isinstance(root_directory, str)

    dataframe = load_main_data(
        root_directory=root_directory,
        usecols=[source.value],
    )

    series = (
        dataframe[source]
        .dropna()
        .astype(str)
        .str.replace(r"\s*;\s*", ";", regex=True)
        .str.split(";")
        .explode()
        .str.strip()
    )

    if (series == "").any():
        raise AssertionError(f'Empty term found in column "{source}"')
