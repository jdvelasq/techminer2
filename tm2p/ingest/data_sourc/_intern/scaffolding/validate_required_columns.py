from pathlib import Path

import pandas as pd  # type: ignore

from tm2p.enums import CorpusField

MAIN_COLUMNS = frozenset(
    [
        CorpusField.ABSTR_RAW.value,
        CorpusField.AUTHID_RAW.value,
        CorpusField.AUTH_RAW.value,
        CorpusField.AUTHKW_RAW.value,
        CorpusField.GCS.value,
        CorpusField.PUBTYPE_RAW.value,
        CorpusField.DOI.value,
        CorpusField.IDXKW_RAW.value,
        CorpusField.PG_FIRST.value,
        CorpusField.YEAR.value,
        CorpusField.REF_RAW.value,
        CorpusField.SRC_ISO4_RAW.value,
        CorpusField.SRC_RAW.value,
        CorpusField.TITLE_RAW.value,
        CorpusField.VOL.value,
    ]
)

REF_COLUMNS = frozenset(
    [
        CorpusField.AUTHID_RAW.value,
        CorpusField.AUTH_RAW.value,
        CorpusField.PG_FIRST.value,
        CorpusField.YEAR.value,
        CorpusField.SRC_ISO4_RAW.value,
        CorpusField.SRC_RAW.value,
        CorpusField.TITLE_RAW.value,
        CorpusField.VOL.value,
    ]
)


def validate_required_columns(root_directory: str) -> int:

    processed_dir = Path(root_directory) / "ingest" / "processed"
    main_file = processed_dir / "main.csv.zip"
    references_file = processed_dir / "references.csv.zip"

    dataframe = pd.read_csv(
        main_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    main_columns_present = MAIN_COLUMNS.issubset(set(dataframe.columns))
    if not main_columns_present:
        missing_columns = MAIN_COLUMNS.difference(set(dataframe.columns))
        raise AssertionError(
            f"The main file is missing the following required columns: {missing_columns}"
        )

    if not references_file.exists():
        return 1

    dataframe = pd.read_csv(
        references_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    ref_columns_present = REF_COLUMNS.issubset(set(dataframe.columns))
    if not ref_columns_present:
        missing_columns = REF_COLUMNS.difference(set(dataframe.columns))
        raise AssertionError(
            f"The references file is missing the following required columns: {missing_columns}"
        )

    return 2
