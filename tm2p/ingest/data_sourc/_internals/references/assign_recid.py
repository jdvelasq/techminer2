from pathlib import Path

import numpy as np
import pandas as pd  # type: ignore

from tm2p import CorpusField


def _get_author(dataframe):
    return dataframe[CorpusField.AUTH_NORM.value].map(
        lambda x: (
            x.split("; ")[0].strip().split()[0] if not pd.isna(x) else "[Anonymous]"
        )
    )


def _get_source_title(dataframe):

    source_title = dataframe[CorpusField.SRC_ISO4_NORM.value].copy()
    source_title_isna = source_title.map(pd.isna)
    source_title = pd.Series(
        np.where(
            source_title_isna,
            dataframe[CorpusField.SRC_NORM.value].str[:29],
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
    return dataframe[CorpusField.YEAR.value].map(str)


def _get_volume(dataframe):
    return dataframe[CorpusField.VOL.value].map(
        lambda x: ", V" + str(x).replace(".0", "") if not pd.isna(x) else ""
    )


def _get_page_start(dataframe):
    return dataframe[CorpusField.PG_FIRST.value].map(
        lambda x: ", P" + str(x).replace(".0", "") if not pd.isna(x) else ""
    )


def assign_recid(root_directory: str) -> int:

    #
    # Create a WoS style reference column.
    # First Author, year, source_title_abbr, 'V'volumne, 'P'page_start, ' DOI ' doi
    #
    path = Path(root_directory) / "ingest" / "processed"

    for file in ["references.csv.zip", "main.csv.zip"]:

        database_file = path / file

        if file == "references.csv.zip" and not database_file.exists():
            continue

        if file == "main.csv.zip" and not database_file.exists():
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
            wos_ref.loc[index] += ", " + dataframe[CorpusField.TITLE_RAW.value].loc[
                index
            ].str[:29].str.upper().str.replace(".", "").str.replace(
                " - ", " "
            ).str.replace(
                ",", ""
            ).str.replace(
                ":", ""
            ).str.replace(
                "-", ""
            ).str.replace(
                "'", ""
            )

        dataframe[CorpusField.RID.value] = wos_ref.copy()
        dataframe = dataframe.drop_duplicates(subset=[CorpusField.RID.value])

        non_null_count = int(dataframe[CorpusField.RID.value].notna().sum())

        dataframe.to_csv(
            database_file,
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )

    return non_null_count
