"""

Smoke test:
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "authors_norm": ["Doe, J.; Doe, J.", "Smith, A."],
    ...     "author_ids_norm": ["id1; id2", "id3"]
    ... })
    >>> mapping = _build_author_mapping(df)
    >>> mapping["id1"]
    'Doe, J.'
    >>> mapping["id2"]
    'Doe, J./1'

"""

from pathlib import Path

import pandas as pd  # type: ignore

from techminer2 import CorpusField

from ..operations import DataFile, transform_column


def _load_authors_data(root_directory: Path) -> pd.DataFrame:

    main_file = root_directory / "data" / "processed" / "main.csv.zip"
    ref_file = root_directory / "data" / "processed" / "references.csv.zip"

    if not main_file.exists():
        raise FileNotFoundError(f"{main_file} not found")

    df = pd.read_csv(
        main_file,
        usecols=[
            CorpusField.AUTH_NORM.value,
            CorpusField.AUTH_ID_NORM.value,
        ],
        compression="zip",
        encoding="utf-8",
        low_memory=False,
    )

    if ref_file.exists():

        ref_df = pd.read_csv(
            ref_file,
            usecols=[
                CorpusField.AUTH_NORM.value,
                CorpusField.AUTH_ID_NORM.value,
            ],
            compression="zip",
            encoding="utf-8",
            low_memory=False,
        )
        df = pd.concat([df, ref_df], ignore_index=True)

    return df.dropna()


def _build_author_mapping(df: pd.DataFrame) -> dict[str, str]:

    df[CorpusField.AUTH_NORM.value] = df[CorpusField.AUTH_NORM.value].str.split("; ")
    df[CorpusField.AUTH_ID_NORM.value] = df[CorpusField.AUTH_ID_NORM.value].str.split(
        "; "
    )

    df = df.explode(
        [
            CorpusField.AUTH_NORM.value,
            CorpusField.AUTH_ID_NORM.value,
        ]
    )

    df[CorpusField.AUTH_NORM.value] = df[CorpusField.AUTH_NORM.value].str.strip()
    df[CorpusField.AUTH_ID_NORM.value] = df[CorpusField.AUTH_ID_NORM.value].str.strip()

    df = df.drop_duplicates(subset=[CorpusField.AUTH_ID_NORM.value])

    df = df.sort_values(CorpusField.AUTH_NORM.value)
    df["counter"] = df.groupby(CorpusField.AUTH_NORM.value).cumcount()

    mask_collision = df["counter"] > 0
    df.loc[mask_collision, CorpusField.AUTH_NORM.value] += "/" + df.loc[
        mask_collision, "counter"
    ].astype(str)

    return dict(
        zip(
            df[CorpusField.AUTH_ID_NORM.value],
            df[CorpusField.AUTH_NORM.value],
        )
    )


def disambiguate_auth_norm(root_directory: str) -> int:

    root = Path(root_directory)

    raw_data = _load_authors_data(root)
    id_to_name = _build_author_mapping(raw_data)

    def _apply_normalization(series: pd.Series) -> pd.Series:
        return series.str.split(";").map(
            lambda ids: (
                "; ".join([id_to_name[x.strip()] for x in ids])
                if isinstance(ids, list)
                else None
            )
        )

    count = transform_column(
        source=CorpusField.AUTH_ID_NORM,
        target=CorpusField.AUTH_DISAMB,
        function=_apply_normalization,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )

    count += transform_column(
        source=CorpusField.AUTH_ID_NORM,
        target=CorpusField.AUTH_DISAMB,
        function=_apply_normalization,
        root_directory=root_directory,
        file=DataFile.REFERENCES,
    )

    return count
