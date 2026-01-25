import re
from pathlib import Path

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr

ACRONYMS_PATTERN = re.compile(r"\((.*?)\)")


def _extract_acronyms_from_text(text: str) -> str:
    if pd.isna(text):
        return ""
    matches = ACRONYMS_PATTERN.findall(text)
    return "; ".join(matches)


def normalize_acronyms(root_directory: str, source: str, target: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return 0

    with stdout_to_stderr():
        pandarallel.initialize(progress_bar=True, verbose=2)
        dataframe[target] = dataframe[source].parallel_apply(_extract_acronyms_from_text)  # type: ignore[call-arg]

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())
