import re
from pathlib import Path

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr

_COMPILED_PATTERNS: list[re.Pattern] = []


def _get_compiled_patterns(root_directory: str) -> list[re.Pattern]:
    if not _COMPILED_PATTERNS:
        urls_file = Path(root_directory) / "data" / "my_keywords" / "urls.txt"
        with urls_file.open("r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
        _COMPILED_PATTERNS.extend(
            re.compile(r"(" + url + r")", re.IGNORECASE) for url in urls
        )
    return _COMPILED_PATTERNS


def repair_urls(root_directory: str, source: str, target: str) -> int:

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
        pandarallel.initialize(progress_bar=True)

    compiled_patterns = _get_compiled_patterns(root_directory)

    def _repair_url(text):
        if pd.isna(text):
            return text
        text = str(text)
        for pattern in compiled_patterns:
            text = pattern.sub(lambda m: m.group().lower(), text)
        return text

    with stdout_to_stderr():
        dataframe[target] = dataframe[source].parallel_apply(_repair_url)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())
