"""

Smoke test:
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "authors": ["Doe, J.; Doe, J.", "Smith, A."],
    ...     "author_ids": ["id1; id2", "id3"]
    ... })
    >>> mapping = _build_author_mapping(df)
    >>> mapping["id1"]
    'Doe, J.'
    >>> mapping["id2"]
    'Doe, J./1'

"""

from pathlib import Path

import pandas as pd  # type: ignore

from techminer2 import Field

from ..operations import DataFile, transform_column


def _load_authors_data(root_directory: Path) -> pd.DataFrame:

    data_path = root_directory / "data" / "processed"
    main_file = data_path / "main.csv.zip"

    if not main_file.exists():
        raise FileNotFoundError(f"{main_file} not found")

    df = pd.read_csv(
        main_file,
        usecols=["authors", "author_ids"],
        compression="zip",
        encoding="utf-8",
        low_memory=False,
    )

    ref_file = data_path / "references.csv.zip"

    if ref_file.exists():

        ref_df = pd.read_csv(
            ref_file,
            usecols=["authors", "author_ids"],
            compression="zip",
            encoding="utf-8",
            low_memory=False,
        )
        df = pd.concat([df, ref_df], ignore_index=True)

    return df.dropna()


def _build_author_mapping(df: pd.DataFrame) -> dict[str, str]:

    df = df.assign(
        authors=df["authors"].str.split("; "),
        author_ids=df["author_ids"].str.split("; "),
    ).explode(["authors", "author_ids"])

    df["authors"] = df["authors"].str.strip()
    df["author_ids"] = df["author_ids"].str.strip()

    df = df.drop_duplicates(subset=["author_ids"])

    df = df.sort_values("authors")
    df["counter"] = df.groupby("authors").cumcount()

    mask_collision = df["counter"] > 0
    df.loc[mask_collision, "authors"] += "/" + df.loc[mask_collision, "counter"].astype(
        str
    )

    return dict(zip(df["author_ids"], df["authors"]))


def disambiguate_authors(root_directory: str) -> int:

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
        source=Field.AUTH_ID,
        target=Field.AUTH,
        function=_apply_normalization,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )

    count += transform_column(
        source=Field.AUTH_ID,
        target=Field.AUTH,
        function=_apply_normalization,
        root_directory=root_directory,
        file=DataFile.REFERENCES,
    )

    return count
