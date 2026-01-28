from pathlib import Path

import numpy as np
import pandas as pd  # type: ignore


def _get_author(dataframe):
    return dataframe.authors.map(
        lambda x: x.split("; ")[0].strip() if not pd.isna(x) else "[Anonymous]"
    )


def _get_source_title(dataframe):

    source_title = dataframe.source_title_abbr.copy()
    source_title_isna = source_title.map(pd.isna)
    source_title = pd.Series(
        np.where(
            source_title_isna,
            dataframe.source_title.str[:29],
            source_title,
        )
    )

    return (
        source_title.str.upper()
        .str.replace("JOURNAL", "J")
        .str.replace(" OF ", " ")
        .str.replace(".", "")
        .str.replace(" - ", " ")
        .str.replace(",", "")
        .str.replace(":", "")
        .str.replace("-", "")
        .map(lambda x: x if not pd.isna(x) else "")
    )


def _get_year(dataframe):
    return dataframe.year.map(str)


def _get_volume(dataframe):
    return dataframe.volume.map(
        lambda x: ", V" + str(x).replace(".0", "") if not pd.isna(x) else ""
    )


def _get_page_start(dataframe):
    return dataframe.page_start.map(
        lambda x: ", P" + str(x).replace(".0", "") if not pd.isna(x) else ""
    )


def assign_record_id(root_directory: str) -> int:

    #
    # Create a WoS style reference column.
    # First Author, year, source_title_abbr, 'V'volumne, 'P'page_start, ' DOI ' doi
    #

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    wos_ref = (
        _get_author(dataframe)
        + ", "
        + _get_year(dataframe)
        + ", "
        + _get_source_title(dataframe)
        + _get_volume(dataframe)
        + _get_page_start(dataframe)
    )

    index = wos_ref[wos_ref.duplicated()].index
    if len(index) > 0:
        wos_ref.loc[index] += ", " + dataframe.document_title.loc[index].str[
            :29
        ].str.upper().str.replace(".", "").str.replace(" - ", " ").str.replace(
            ",", ""
        ).str.replace(
            ":", ""
        ).str.replace(
            "-", ""
        ).str.replace(
            "'", ""
        )

    dataframe["record_id"] = wos_ref.copy()
    dataframe = dataframe.drop_duplicates(subset=["record_id"])

    non_null_count = int(dataframe["record_id"].notna().sum())

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return non_null_count
