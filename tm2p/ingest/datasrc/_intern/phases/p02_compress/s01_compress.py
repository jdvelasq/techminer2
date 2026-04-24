# CODE_REVIEW: 2026-01-26

import zipfile
from pathlib import Path

import pandas as pd  # type: ignore

from ..get_datab_marker import get_datab_marker


def s01_compress(root_directory: str) -> int:

    common_kwargs = {"root_directory": root_directory}

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _openalex,
        "PubMed": _pubmed,
        "Scopus": _openalex,
        "WoS": _wos,
    }.get(marker)

    if function is not None:
        function(**common_kwargs)

    return 1


def _wos(root_directory: str) -> None:

    filepath = Path(root_directory) / "ingest" / "raw"
    csv_files = list(filepath.glob("*.csv"))

    for csv_file in csv_files:
        zip_file = str(csv_file) + ".zip"
        df = pd.read_csv(csv_file, encoding="utf-8", low_memory=False, sep="\t")
        df.to_csv(zip_file, index=False, encoding="utf-8", compression="zip")
        csv_file.unlink()


def _openalex(root_directory: str) -> None:

    filepath = Path(root_directory) / "ingest" / "raw"
    csv_files = list(filepath.glob("*.csv"))

    for csv_file in csv_files:
        zip_file = str(csv_file) + ".zip"
        df = pd.read_csv(csv_file, encoding="utf-8", low_memory=False)
        df.to_csv(zip_file, index=False, encoding="utf-8", compression="zip")
        csv_file.unlink()


def _pubmed(root_directory: str) -> None:

    filepath = Path(root_directory) / "ingest" / "raw"
    txt_files = list(filepath.glob("*.txt"))

    for txt_file in txt_files:
        zip_file = txt_file.with_suffix(".txt.zip")
        with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(txt_file, arcname=txt_file.name)
        txt_file.unlink()
