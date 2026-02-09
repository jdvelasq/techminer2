from pathlib import Path

import pandas as pd  # type: ignore

from techminer2.enums import CorpusField

MAIN_COLUMNS = frozenset(
    [
        CorpusField.ABS_RAW.value,
        CorpusField.AUTH_ID_RAW.value,
        CorpusField.AUTH_RAW.value,
        CorpusField.AUTH_KEY_RAW.value,
        CorpusField.CIT_COUNT_GLOBAL.value,
        CorpusField.DOCTYPE_RAW.value,
        CorpusField.DOI.value,
        CorpusField.IDX_KEY_RAW.value,
        CorpusField.PAGE_FIRST.value,
        CorpusField.PUBYEAR.value,
        CorpusField.REF_RAW.value,
        CorpusField.SRCTITLE_ABBR_RAW.value,
        CorpusField.SRCTITLE_RAW.value,
        CorpusField.DOCTITLE_RAW.value,
        CorpusField.VOL.value,
    ]
)

REF_COLUMNS = frozenset(
    [
        CorpusField.AUTH_ID_RAW.value,
        CorpusField.AUTH_RAW.value,
        CorpusField.PAGE_FIRST.value,
        CorpusField.PUBYEAR.value,
        CorpusField.SRCTITLE_ABBR_RAW.value,
        CorpusField.SRCTITLE_RAW.value,
        CorpusField.DOCTITLE_RAW.value,
        CorpusField.VOL.value,
    ]
)


def validate_required_columns(root_directory: str) -> int:

    processed_dir = Path(root_directory) / "data" / "processed"
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
