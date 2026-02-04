from pathlib import Path

import pandas as pd  # type: ignore

from techminer2.enums import Field

MAIN_COLUMNS = frozenset(
    [
        Field.ABS_RAW.value,
        Field.AUTH_ID_RAW.value,
        Field.AUTH_RAW.value,
        Field.AUTH_KEY_RAW.value,
        Field.CIT_COUNT_GLOBAL.value,
        Field.DOC_TYPE_RAW.value,
        Field.DOI.value,
        Field.IDX_KEY_RAW.value,
        Field.PAGE_FIRST.value,
        Field.PUBYEAR.value,
        Field.REF_RAW.value,
        Field.SRC_TITLE_ABBR_RAW.value,
        Field.SRC_TITLE_RAW.value,
        Field.TITLE_RAW.value,
        Field.VOL.value,
    ]
)

REF_COLUMNS = frozenset(
    [
        Field.AUTH_ID_RAW.value,
        Field.AUTH_RAW.value,
        Field.PAGE_FIRST.value,
        Field.PUBYEAR.value,
        Field.SRC_TITLE_ABBR_RAW.value,
        Field.SRC_TITLE_RAW.value,
        Field.TITLE_RAW.value,
        Field.VOL.value,
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
