"""Replace journal name in references. """

import pathlib

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ..._dtypes import DTYPES
from ._message import message


def replace_journal_name_in_references(root_dir):
    """Replace journal name in references."""

    message("Replacing journal name in references")

    abbrs = []

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data = data[["source", "abbr_source_title"]]
        data = data.dropna()
        data = data.drop_duplicates()
        abbrs.append(data)
    abbrs = pd.concat(abbrs, ignore_index=True)

    main_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
    main = pd.read_csv(main_path, encoding="utf-8", compression="zip", dtype=DTYPES)

    for source, abbr_source_title in tqdm(
        zip(abbrs.source, abbrs.abbr_source_title), total=len(abbrs)
    ):
        main["raw_global_references"] = main["raw_global_references"].str.replace(
            source, abbr_source_title, regex=False
        )
    main.to_csv(main_path, sep=",", encoding="utf-8", index=False, compression="zip")
